#!/bin/bash

#SBATCH --job-name=trimmomatic				# Job name
#SBATCH --mail-type=ALL				# Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user=abc@gmail.com				# Where to send mail
#SBATCH --nodes=1				# Number of nodes requested
#SBATCH --ntasks=16				# Number of CPUs (processor cores/tasks)
#SBATCH --mem=10gb				# Memory limit
#SBATCH --time=01:00:00				# Time limit hrs:min:sec
#SBATCH --partition=short				# Partition/queue requested on server
#SBATCH --output=/Users/dara6367/example/eofiles/%x.%j.out				# Standard output 
#SBATCH --error=/Users/dara6367/example/eofiles/%x.%j.err				# Standard error log 


### Displays the job context 
echo Job: $SLURM_JOB_NAME with ID $SLURM_JOB_ID 
echo Running on host `hostname` 
echo Job started at `date +"%T %a %d %b %Y` 
echo Directory is `pwd` 
echo Using $SLURM_NTASKS processors across $SLURM_NNODES nodes 


### Assigns path variables 
DIRECTORY=/Users/dara6367/example 


### Loads modules 
module load trimmomatic/0.36 

### Runs fastQC 
java -jar /opt/trimmomatic/0.36/trimmomatic-0.36.jar SE -threads 16 -phred33 \
-trimlog $DIRECTORY/trimmomatic/AthaChIPfarRedLight.trimlog \ 
$DIRECTORY/fastq/AthaChIPfarRedLight.fastq \
$DIRECTORY/trimmomatic/AthaChIPfarRedLight.trimmed.fastq \
ILLYMINACLIP:/opt/trimmomatic/0.36/adapters/TruSeq3-PE-2.fa:2:30:10 \
LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36

### Final time stamp
echo job finished at `date +"%T %a %d %b %Y`
