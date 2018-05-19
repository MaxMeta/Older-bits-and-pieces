#!/bin/sh
#This script will take a fastq file, phred trim it using seqTK with standard parameters and blast the resulting fasta
#Current blast DB is a small collection of complete gene clusters (MiBig)
#Blast Params are unusual, compare these to defaults, you may want to alter
#this will run for ~2.5 hrs with 24 cores + 8 Gb ram to complete a ~300 mb fastq file of 100 bp HiSeq reads
#Will run (much) longer for a larger blast DB 
####################################################################
#qsub parameters go here
#$ -S /bin/sh
#this should always be 1
#$ -l h_slots=1
#set the maximum run time for in seconds - in this case 86400=1 day
#$ -l s_rt=40000
#the maximum memory you expect the job to use

#$ -l mem_total=8G
#the total virtual memory you want set aside for the job (same as above?)
#$ -l virtual_free=24G
#the number of threads (cores) you want allocated to the job
#$ -pe smp 24
####################################################################


#This sets up  temporary directories for I/O from the job
WDIR=$GLOBAL_SCRATCH/$JOB_NAME-$JOB_ID
OUTDIR=$GLOBAL_SCRATCH/OUTPUTS/$JOB_NAME-$JOB_ID
export WDIR
export OUTDIR
mkdir -p $WDIR
mkdir -p $OUTDIR
DataDir=$GLOBAL_SCRATCH/seqdat1
export DataDir
PATH="$PATH:$HOME/bin:$HOME/ncbi-blast-2.3.0+/bin"
export PATH
BLASTDB="$HOME/ncbi-blast-2.3.0+/db"
export BLASTDB

#if the above didn't work then just quit.
if [ ! -d $WDIR  ]||[ ! -d $OUTDIR  ]; then #add an or not outdir exists bit
        echo "There's no job directory to change into therefore I exit..."
        exit 1
fi

cd $WDIR #Change to the working directory you just created


DataDir=$GLOBAL_SCRATCH/seqdat1
touch $OUTDIR/times.txt
for filename in $DataDir/*
 do
    base=$(basename $filename)
    NoExt=${base%%.*}
    outname=$NoExt.blastout.txt 
    t=$(date)
    echo "started processing $NoExt the time is $t" >> $OUTDIR/times.txt #stamp the start time for the file
    cp $filename . #copy it to the working directory
    
    seqtk trimfq $base | seqtk seq -A > $NoExt.fa #unzip, quality filter and convert fastq.gz to fasta
    
    blastn -query $NoExt.fa -db $BLASTDB/original_mibig.fna -word_size 9 -num_threads $NSLOTS \
    -outfmt 6 -evalue 0.01 -out $outname -parse_deflines -max_target_seqs 1

    cd ~.fa $base # immediately remove the zipped and unzipped files
    mv $outname $OUTDIR #move the output file to the desired folder
    t=$(date)
    echo "finished processing $NoExt the time is $t" >> $OUTDIR/times.txt #stamp the end time for the file then add a blank line
    echo "" >> $OUTDIR/times.txt
 done

rm -rf $WDIR #remove the temporary folder 

