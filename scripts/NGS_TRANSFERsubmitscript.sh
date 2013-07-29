#!/bin/bash
#$ -S /bin/bash
#$ -P sasc
#$ -q all.q
#$ -N NGS_TXVM31
#$ -cwd
#$ -j Y
#$ -V
#$ -m be
#$ -M w.y.leung@lumc.nl
#$ -pe BWA 1
echo Start time : `date`

bash start_transfer.sh

echo End time : `date`
