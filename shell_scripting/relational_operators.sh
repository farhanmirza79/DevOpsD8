#!/bin/bash
#Author: Mirza
#Relation operators in shell

a=20
b=40

if [ $a -eq $b ]; then
	echo "$a is equal to $b"
else
	echo "$a is not equal to $b"
fi

if [ $a -ne $b ]; then
	echo "$a is not equal to $b"
else
	echo "$a is equal to $b"
fi

if [ $a -lt $b ]; then
	echo "$a is less than $b"
else 
	echo "$a is greater than $b"
fi

if [ $a -ge $b ]; then
	echo "$a is greater or equal to $b"
else 
	echo "$a is lesser than $b"
fi

if [ $a -le $b ]; then
        echo "$a is less than  or equal to $b"
else
        echo "$a is greater than $b"
fi

if [ $a -lt $b -o $a -eq $b ]; then
        echo "$a is less than or equal to $b"
fi

if [ $a -lt $b -a $a -eq $b ]; then
        echo "$a is less than or equal to $b"
fi

