#!/bin/bash

# query for current workdir
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

/usr/bin/time sftp -b $DIR/transfer_files.sftpb sasc@145.88.22.31

