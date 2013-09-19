#!/usr/bin/env python2

####
__description__ = "Reads and parses the /usr/bin/time output to nice dictionary"
####


import argparse, os, sys, collections
import pickle
import re
import string 


def startswithDEBUG(x):
    """
        Filter out the DEBUG lines in the master.log
    """
    if not x.startswith('DEBUG'):
        return x
    else:
        return ''

def parseLine( l ):
    """
        Split the /usr/bin/time output by ": " (semicolon space)
    """
    if len( set(["exited", "terminated"]) - set(l.split(" ")) ) == 1:
        signal_code = l.split(' ')[-1]
        return {'exitcode': signal_code}
    
    pl = map(string.strip,l.split(': '))
    try:
        return {mapTimeStat(pl[0]): pl[1]}
    except:
        print pl
    

def mapTimeStat( key ):
    """
        map the keys defined in the /usr/bin/time stat to more logical keys for python
    """
    keys = {
    "Command being timed": "cmd",
    "User time (seconds)": "utime",
    "System time (seconds)": "stime",
    "Percent of CPU this job got": "rcpu",
    "Elapsed (wall clock) time (h:mm:ss or m:ss)": "wall",
    "Average shared text size (kbytes)": "shmem",
    "Average unshared data size (kbytes)": "unsharedmem",
    "Average stack size (kbytes)": "avg_stacksize",
    "Average total size (kbytes)": "avg_totalsize",
    "Maximum resident set size (kbytes)": "max_mem",
    "Average resident set size (kbytes)": "avg_mem",
    "File system inputs": "fs_input", # in kb
    "File system outputs": "fs_output", # in kb
    "Socket messages sent": "socket_messages_tx",
    "Socket messages received": "socket_messages_rx",
    "Swaps": "context_swaps",
    "Voluntary context switches": "vol_context_switches",
    "Involuntary context switches": "forced_context_switches",
    "Page size (bytes)": "pagesize",
    "Minor (reclaiming a frame) page faults": "page_faults_minor",
    "Major (requiring I/O) page faults": "page_faults_majors",
    "Exit status": "exitcode",
    "Signals delivered": "signals_rx",
    }
    # return the mapped key and otherwise, return original keys
    return keys.get( key, key )
    

def parseIndividualLog( fname=None ):
    """
        fname: the prefixname for the log
        in this case we parse the <fname>.stat.log
    """
    out = {}

    try:
        fd = open( "%s.stat.log" % (fname,), 'r')
    except:
        pass
    else:
        stat = map( parseLine, [line for line in fd] )
        # TODO: ugly construct
        for statline in stat:
            out.update(statline)
    return out
            

def listMasterLog( fname='master.log' ):
    out = ''
    with open( fname, 'r') as fd:
        loglines = [startswithDEBUG(l) for l in fd]
    loglines = list(set(loglines) ^ set(' '))
    loglines="\n".join(loglines)
    
    # post-parse the Log.session.random: command as k:v
    parsed_loglines = re.findall(r'^([\w\d\.]+): ([\_\>\<\*\;\(\)\[\]\"\'\/\=\-\w\d\.\ ]+)\n$', loglines, re.I | re.M)
    # timsort the results
    parsed_loglines.sort()
    return parsed_loglines

def parseAllLogs( loglist, verbose=False ):
    """
        Parse all logentries in loglist into dictionaries
    """
    out = collections.OrderedDict()
    for i, item in enumerate(loglist):
        k,v=item
        logdict = parseIndividualLog( fname=k )
        out[ k ] = logdict
        if verbose:
            print "%5s %s %30s %s" % (i,logdict['utime'],k,v)
    return out

def storePickleLogs( parsed_logs, fname_output ):
    with open( fname_output, 'wb' ) as fd:
        pkl = pickle.dump( parsed_logs, fd )
        

def main():
    '''
    Execute main function taking arguments
    '''
    parser = argparse.ArgumentParser(description=__description__)

    switches = parser.add_argument_group(title='Actions',description='Action to perform')

    switches.add_argument('-l','--list', dest='list', action='store_true',
        help='Print the list of Makelogs')
    switches.add_argument('-p','--parse', dest='parse', action='store_true',
        help='Parse all logs and output pickle to file specified in -o')

    output = parser.add_argument_group(title='Input/Output',description='Argument that involve the output destination')
    output.add_argument('-o','--output', dest='output', default='output.pkl', action='store',
        help='Output file for parsed logfiles (pickle with dictionary formated logentries)')


    args = parser.parse_args()
    if args.list:
        print listMasterLog()
    if args.parse:
        loglist = listMasterLog()
        parsed_logs = parseAllLogs( loglist )
        # store the dictionaries
        storePickleLogs( parsed_logs, args.output )
        
        
        
        

if __name__ == "__main__":
    main()
