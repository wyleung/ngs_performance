#!/bin/bash

# query for current workdir
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

/usr/bin/time sftp -b $DIR/transfer_files.sftpb ngs_performance-lumc@virdir.cloud.sara.nl

