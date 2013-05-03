TARGET_LOCAL=/virdir_lumc/Scratch/usr/local
TARGET=/usr/local
DIRECTORIES="stampy bwa pindel BEDtools samtools picard-tools breakdancer circos sickle FastQC bin"

for d in $DIRECTORIES;
do
    rsync -avzx --progress wyleung@shark:$TARGET/$d $TARGET_LOCAL
done;

