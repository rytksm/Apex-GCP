#! /bin/sh
# $1 filename
# $2 parameter name
# $3 result_file
string=`cat ~/.gcp/$1`
echo $2=$string > $3
echo section=end >> $3

