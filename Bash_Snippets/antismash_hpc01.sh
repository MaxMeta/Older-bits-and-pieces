
#!/bin/sh
#This script will take a folder of nucleic acid sequence files and run antismash on them
####################################################################
#qsub parameters go here
#$ -S /bin/sh
#this should always be 1
#$ -l h_slots=1
#set the maximum run time for in seconds - in this case 86400=1 day
#$ -l s_rt=40000
#the maximum memory you expect the job to use

#$ -l mem_total=16G
#the total virtual memory you want set aside for the job
#$ -l virtual_free=24G
#the number of threads (cores) you want allocated to the job
#$ -pe smp 48
####################################################################


#This sets up  temporary directories for I/O from the job
WDIR=/home/metamax/jeremy/working_dirs/$1
OUTDIR=/home/metamax/jeremy/ISME_antismash/$1

export WDIR
export OUTDIR

mkdir -p $WDIR
mkdir -p $OUTDIR




#if the above didn't work then just quit.
if [ ! -d $WDIR  ]||[ ! -d $OUTDIR  ]; then #add an or not outdir exists bit
        echo "There's no job directory to change into therefore I exit..."
        exit 1
fi

cd $WDIR #Change to the working directory you just created

#set the data directory with a command line argu
DataDir=$GLOBAL_SCRATCH/$1
export DataDir
#make the time stamp file
touch $OUTDIR/times.txt

for filename in $DataDir/*
 do
    base=$(basename $filename)
    NoExt=${base%.*}
    AntiDir=$OUTDIR/$NoExt
    t=$(date)

    echo "started processing $NoExt the time is $t" >> $OUTDIR/times.txt #stamp the start time for the file
    cp $filename . #copy zipped file to the working directory
    gunzip $base #unzip the file, assuming all files are going to be .gz files from NCBI FTP server

    antismash $NoExt --cpus $NSLOTS --smcogs --inclusive --full-hmmer --enable-BiosynML --outputfolder $AntiDir

    t=$(date)
    echo "finished processing $NoExt the time is $t" >> $OUTDIR/times.txt #stamp the end time for the file then add a blank line
    rm -f $NoExt #remove the input file that you copied over
    echo "" >> $OUTDIR/times.txt

 done

rm -rf $WDIR #remove the temporary folder 
