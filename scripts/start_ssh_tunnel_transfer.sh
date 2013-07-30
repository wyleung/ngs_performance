#!/bin/bash

# query for current workdir
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

/usr/bin/time sftp -b $DIR/transfer_files.sftpb -P 2222 -i ~/.ssh/id_dsa ngs_performance-lumc@145.88.22.31
# on target host:
# sysctl net.ipv4.ip_forward=1
# iptables -A PREROUTING -t nat -i eth2 -p tcp --dport 2222 -j DNAT --to-destination 10.0.103.4:22
# iptables -t nat -A POSTROUTING -j MASQUERADE -o eth0 -s 145.88.22.0/24

