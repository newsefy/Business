cd $1
ls > filelist
while read line;
do
	new=$2$line
	mv $line $new
done <filelist

remove=$2'filelist'
rm $remove
