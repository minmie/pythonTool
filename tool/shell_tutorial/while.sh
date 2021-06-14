#!/bin/sh


n=1
while [ $n -lt 5 ]
do
    echo "n is $n"
    let "n++"
done
