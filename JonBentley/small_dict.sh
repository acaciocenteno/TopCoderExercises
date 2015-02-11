#!/bin/bash

# Shamelessly create a small dict file by taking ranges from the system's dict

if [ $# -gt 0 ]; then
	offset=$1
else
	offset=50
fi

file=/usr/share/dict/words
out=small.txt
len=`wc -l ${file}|awk '{print $1}'`
half=$((len/2))
beg=$((half-(offset/2)))
end=$((half+(offset/2)))

# Take offset from the beginning
head -${offset} ${file} | tr '[A-Z]' '[a-z]' > ${out}
# Take offset from the middle
head -${end} ${file} | tail -${offset} | tr '[A-Z]' '[a-z]' >> ${out}
# Take offset from the end
tail -${offset} ${file} | tr '[A-Z]' '[a-z]' >> ${out}
# Make sure ours known anagrams are in the game
echo "deposit" >> ${out}
echo "dopiest" >> ${out}
echo "posited" >> ${out}
echo "topside" >> ${out}