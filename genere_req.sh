#!/bin/sh

base=`pwd`

recur(){
	cd $1
	echo `pwd`

	jupyter nbconvert --to=python *.ipynb >/dev/null 2>/dev/null
	pipreqs --force . >/dev/null 2>/dev/null
	
	for f in `ls *.ipynb 2>/dev/null`; do 
		rm $(echo "$f" | sed "s/ipynb/py/") 2>/dev/null
	done;

	if [ "$base" != `pwd` ]; then
		cat ./requirements.txt >> "$base/requirements.txt" 2>/dev/null
	fi;

	for d in `ls`; do
		if [ -d $d ]; then
			echo "d:$d"
			recur $d
		fi;
	done;
}

recur ./
cd $base
cat ./requirements.txt | sort | uniq > ./requirements2.txt
mv ./requirements2.txt ./requirements.txt
