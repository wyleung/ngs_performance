#!/usr/bin/env python2
####
__description__ = "Reads and parses the /usr/bin/time output to nice dictionary"
__author__ = "Wai Yi Leung"
__contact__ = "w DOT y DOT leung <a> lumc DOT nl"
__version__ = (0,0,2)
__licence__ = "MIT"
__organisation__ = "Leiden University Medical Centre"
__copyright__ = "%s - %s 2013" % (__author__, __organisation__)
####


import argparse, os, sys, collections
import pickle
import re
import string

class TimeStatParser(object):
    def __init__(self, *args, **kwargs):
        self.verbosity = kwargs.get('verbosity', False)
        self.output = kwargs.get('output', None)
        self.data = None
        self.loglist = None
        self.statkeys = {
            "Command being timed":                  "cmd",
            "User time (seconds)":                  "utime",
            "System time (seconds)":                "stime",
            "Percent of CPU this job got":          "rcpu",
            "Elapsed (wall clock) time (h:mm:ss or m:ss)": "wall",
            
            "Average shared text size (kbytes)":    "shmem",
            "Average unshared data size (kbytes)":  "unsharedmem",
            "Average stack size (kbytes)":          "avg_stacksize",
            "Average total size (kbytes)":          "avg_totalsize",
            "Maximum resident set size (kbytes)":   "max_mem",
            "Average resident set size (kbytes)":   "avg_mem",

            "File system inputs":                   "fs_input", # in kb
            "File system outputs":                  "fs_output", # in kb

            "Socket messages sent":                 "socket_messages_tx",
            "Socket messages received":             "socket_messages_rx",
            "Swaps":                                "context_swaps",

            "Voluntary context switches":           "vol_context_switches",
            "Involuntary context switches":         "forced_context_switches",

            "Page size (bytes)":                    "pagesize",
            "Minor (reclaiming a frame) page faults": "page_faults_minor",
            "Major (requiring I/O) page faults":    "page_faults_majors",

            "Exit status":                          "exitcode",
            "Signals delivered":                    "signals_rx",
        }

    def clean_sh( self, l ):
        if 'sh -c ' in l:
            return l.replace('sh -c ', '')
        return l

    def startswithDEBUG( self, x):
        """
            Filter out the DEBUG lines in the master.log
        """
        if not x.startswith('DEBUG'):
            return self.clean_sh(x)
        else:
            return ''

    def parseLine( self, l ):
        """
            Split the /usr/bin/time output by ": " (semicolon space)
        """
        if len( set(["exited", "terminated"]) - set(l.split(" ")) ) == 1:
            signal_code = l.split(' ')[-1]
            return {'exitcode': signal_code}
        
        pl = map(string.strip,l.split(': '))
        try:
            return {self.mapTimeStat(pl[0]): pl[1]}
        except:
            print pl
        

    def mapTimeStat( self, key ):
        """
            map the keys defined in the /usr/bin/time stat to more logical keys for python
        """
        # return the mapped key and otherwise, return original keys
        return self.statkeys.get( key, key )
        

    def parseIndividualLog( self, fname=None ):
        """
            fname: the prefixname for the log
            in this case we parse the <fname>.stat.log
        """
        log = {}

        try:
            fd = open( "%s.stat.log" % (fname,), 'r')
        except:
            pass
        else:
            stat = map( self.parseLine, [line for line in fd] )
            # TODO: ugly construct
            for statline in stat:
                log.update(statline)
        return log
                

    def listMasterLog( self, fname='master.log' ):
        out = ''
        with open( fname, 'r') as fd:
            loglines = [self.startswithDEBUG(l) for l in fd]
        # clean out empty commands (non-captured commands with pipes invoked from shell)
        loglines = list(set(loglines) ^ set(''))
        loglines="\n".join(loglines)
        
        # post-parse the Log.session.random: command as k:v
        # parsed_loglines = re.findall(r"^([\w\d\.]+): ([\$\_\>\<\*\{\}\(\)\[\]\"\'\|\/\w\d\=\-\,\.\;\ ]+)\n$", loglines, re.I | re.M)
        parsed_loglines = re.findall(r"^([\w\d\.]+): (.*)\n$", loglines, re.I | re.M)
        # timsort the results
        parsed_loglines.sort()
        self.loglist = parsed_loglines
        return parsed_loglines

    def parseAllLogs( self, loglist=None ):
        """
            Parse all logentries in loglist into dictionaries
        """
        if not loglist:
            self.listMasterLog()
            loglist = self.loglist
        
        self.data = collections.OrderedDict()
        if self.verbosity:
            #init some stats variable
            utime_sum = 0.0
        for i, item in enumerate(loglist):
            k,v=item
            logdict = self.parseIndividualLog( fname=k )
            if logdict.get('cmd', '') == '':
                logdict['cmd'] = v
            self.data[ k ] = logdict
            if self.verbosity:
                utime_sum += float( logdict.get('utime',0.00) )
                print "%4s %8s -%25s- %s" % (i,logdict.get('utime','0.00'),k,v)
        if self.verbosity:
            print "{0} seconds taken total for this pipeline run\nRoughly equal to {1} hours (+fractions)".format( utime_sum, round( utime_sum/3600.0, 2) )
        return self.data

    def statistics( self ):
        # generate pivot table
        keys = self.statkeys.values()
        keys.sort()
        # print header first
        print "{0}\t{1}\t{2}".format("Log", "", "\t".join(keys))
        
        for k,log in self.data.items():
            log_info = map( lambda x: self.clean_sh(self.data[k].get(x, '-')), keys)
            print "{0}\t{1}\t{2}".format(k, "", "\t".join(log_info))

    def storePickleLogs( self, fname_output=None ):
        """
            store self.data in 
        """
        assert not self.data == None, "There are no logfiles parsed yet, please parse log first"
        
        if not fname_output:
            fname_output = self.output

        with open( fname_output, 'wb' ) as fd:
            pkl = pickle.dump( self.data, fd )
        

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

    switches.add_argument('-s','--stats', dest='statistics', action='store_true',
        help='Show basic statistics')

    output = parser.add_argument_group(title='Input/Output',description='Argument that involve the output destination')
    output.add_argument('-o','--output', dest='output', default='output.pkl', action='store',
        help='Output file for parsed logfiles (pickle with dictionary formated logentries)')

    output.add_argument('-v','--verbose', dest='verbose', default=False, action='store_true',
        help='Verbose output'
    )

    args = parser.parse_args()
    
    logparser = TimeStatParser( output=args.output, verbosity=args.verbose )
    
    if args.list:
        print logparser.listMasterLog()
    if args.parse:
        parsed_logs = logparser.parseAllLogs()
        # store the dictionaries
        logparser.storePickleLogs()
        
        
    if args.statistics:
        # display some basic statistics (summation?)
        logparser.statistics()
        
        
        

if __name__ == "__main__":
    main()
