#!/bin/bash
#Author: Mirza
#File operators in shell scripting


file="example.txt"

if [ -e $file ]; then
	echo "file exists"
else 
	echo "file doesnt exist"
fi

if [ -f $file ]; then
	echo "$file is a regular file"
else 
	echo "$fiel is not a regular file"
fi

directory="/home/ubuntu"

if [ -d $directory ]; then
	echo "$directory is a directory"
else 
	echo "$directory is not a directory"
fi

if [ -r $file ]; then
	echo "$file is a readable file"
else 
	echo "$file is not a readable file"
fi
