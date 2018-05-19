
#!/bin/sh
NSLOTS=4
WDIR=/home/metamax/jeremy/working_dirs/$1
OUTDIR=/home/metamax/jeremy/ISME_antismash

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
#modify the base directory as needed
DataDir=/home/metamax/jeremy/COG_ISME/$1
export DataDir
#make the time stamp file
touch $OUTDIR/times.txt

for filename in $DataDir/*
 do
    base=$(basename $filename)
#NoExt=${base%.*}
    AntiDir=$OUTDIR/$1\_$base
    t=$(date)

    echo "started processing $filename the time is $t" >> $OUTDIR/times.txt #stamp the start time for the file
    cp $filename . #copy zipped file to the working directory
#gunzip $base #unzip the file, assuming all files are going to be .gz files from NCBI FTP server

    antismash $base --cpus $NSLOTS --smcogs --inclusive --full-hmmer --enable-BiosynML --outputfolder $AntiDir --smcogs --knownclusterblast --transatpks_da --transatpks_da_cutoff 10 --clusterblast

    t=$(date)
    echo "finished processing $NoExt the time is $t" >> $OUTDIR/times.txt #stamp the end time for the file then add a blank line
    rm -f $filename #remove the input file that you copied over
    echo "" >> $OUTDIR/times.txt

 done

rm -rf $WDIR #remove the temporary folder 
