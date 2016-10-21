#!/bin/bash
ps -e | grep zook > killer
cat killer | cut -d' ' -f 2 > temp
a=( $(cat temp ) )
for i in ${a[*]}
do
	kill $i
done
rm killer temp
