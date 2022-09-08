#unix
cat -A (hidden character) (^I means control-I or ASCII 9, also known as TAB)\
cat -t (hidden character)\
cat -E (hidden new line)\

grep -v "#" gene.gtf |cut -f 2 (remove header)\
grep -o -P "gene_id \"S+\"" gene.gtf (using perl regular expression)\
zgrep --max-count=10000 -e "^@" *.fastq.gz | grep -oP "\s\d+" | sort | uniq -c\

awk '(NR>=100 && NR <=200) || ($1 =="chr22")' abc.bed (line 100 and 200 and field 1 match chr22)\
alias awkt='awk -v OFS="\t"' (awk is 1 indexed)\
awk -v OFS="\t" '{print $0,$3-$2}' abc.bed\
awk -v OFS="\t" '{print $0 "\t" $3-$2}' abc.bed\
awk '{print $0,$3-$2}' abc.bed (euqals above)\
awk '$1 ~/chr1/ && $3-$2>100' abc.bed (match, !~ not match)\

cut -f1,2,3 -d$'\t' abc.bed (default tab)\
sed -i 's/old/new/g' input.txt\

sort -k1,1 -k2,2n abc.bed  (chr1, chr2, 10, 11, 22) (col1 by character sort, col2 by numeric sort) (recommended, many programs sorted this way, e.g. bedtools -sorted)\
sort -k1,1V -k2,2n abc.bed (chr1, 2, 10, 11,22)\

ncdu (disk usage)\
du -h -d0 *\
du -h . * \


cat work/xxxxxxxxxxx/.command.sh (nf-core)\
cat work/xxxxxxxxxxx/.command.out\

samtools view -F 4 abc.bam | awk '{print length($10)}' | sort -n | uniq -c \

for f in *.mp4; do ffmpeg -i $f -c copy $f.mkv; done \

outfile = samfyle.replace('.sam','_samtools.sam')\

cat files.txt | xargs rm -rf\
ls *.bam | xargs -i samtools index {}\

export PATH=/userpath/bin:$PATH\

paste *.txt | awk '{printf $1 "\t";for(i=2;i<=NF;i+=2) printf $i"\t";printf $i}' (htseq combine)\


#conda
conda create -n abc python=3.7.6\
conda remove --name abc --all\

#numpy
df.iloc[10:20]\
di.loc[df['type'] == 'abc']\
df.['total'] = df.iloc[:, 4:9].sum(axis=1)\
df.loc[df['total'].str.contains('abc')]\
df.loc[df['total'].str.contains('abc'),flags=re.I] #ignore case\
df.loc[~df['total'].str.contains('abc'),flags=re.I] #not

