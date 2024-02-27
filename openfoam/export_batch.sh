## -----------------------------------------
## Impose to read the script with bash
## -----------------------------------------
#$ -S /bin/bash
echo “cat PE_HOSTFILE:”
cat $PE_HOSTFILE
## -----------------------------------------
## Replace NPROC by the desired number of processors and openmpi by the desired environnement
## -----------------------------------------
#$ -pe openmpi 1
#$ -q omnipath
## -----------------------------------------
## Name of the run
## ----------------------------------------
#$ -N j_exporter
##------------------------------------------
## Change directory to this job's working directory
## -----------------------------------------
#$ -cwd
## -----------------------------------------
## Print start time and present Directory
## -----------------------------------------
echo Start time is `date`
echo Directory is `pwd`
## -----------------------------------------
## Run the executable a.out
## ----------------------------------------- 
source activate env_ml
python -u openfoam_parser.py
## -----------------------------------------
## Echo end time
## -----------------------------------------
echo End time is `date`
