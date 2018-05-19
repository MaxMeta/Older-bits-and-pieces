
#!/bin/sh
export PATH=~/Dropbox/blast/ncbi-blast-2.6.0+/bin:$PATH
export DB=/Users/owenje/Desktop/Cog_LE/Cog
NSLOTS=2
OUTDIR=/Users/owenje/Dropbox/PapersAndData/Pateamine_paper/COG_analysis/COG_Tables/
DataDir=/Users/owenje/Dropbox/PapersAndData/Pateamine_paper/COG_analysis/Single_bin_genomes_gbk/aa_out

export DataDir
export OUTDIR


mkdir -p $OUTDIR

cd $DataDir

touch $OUTDIR/times.txt

for filename in $DataDir/*
 do
    base=$(basename $filename)
    NoExt=${base%%.*}
    OutName=$OUTDIR/$NoExt.txt
    t=$(date)
    echo "started processing $filename the time is $t" >> $OUTDIR/times.txt

    rpsblast -query $base -evalue 0.00001 -db $DB -out $OutName -outfmt 6  -max_target_seqs 1

    t=$(date)
    echo "finished processing $NoExt the time is $t" >> $OUTDIR/times.txt
    echo "" >> $OUTDIR/times.txt

 done


