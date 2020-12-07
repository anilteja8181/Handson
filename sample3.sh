#!/bin/bash
n=10
fact=1
for (( i=1 ; i<=n ; i++ ))
do
fact=$(( fact * i ))
done
echo factorial of $n is $fact
