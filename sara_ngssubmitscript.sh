#!/bin/bash
#$ -S /bin/bash
#$ -P sasc
#$ -q all.q
#$ -N sara_ngs
#$ -cwd
#$ -j Y
#$ -V
#$ -m be
#$ -M w.y.leung@lumc.nl
#$ -pe BWA 1
echo Start time : `date`

bash /data/DIV5/SASC/wyleung/ngs_performance/start_transfer.sh > transfer.log

echo End time : `date`