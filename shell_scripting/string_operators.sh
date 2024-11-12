#!/bin/bash
#autohr: Mirza
#String operators in shell scripting

str_1="Hello"
str_2="Hello"
str_3="world"
str_4=""


if [ $str_1 = $str_2 ]; then
	echo "$str_1 is same as $str_2"
else 
	echo "$str_1 is not same as $str_2"
fi

if [ -z $str_4 ]; then
	echo "$str_4 is an empty string"
else 
	echo "$str_4 is not an empty string"
fi

if [ -n $str_3 ]; then
	echo "$str_3 is non-zero lenth"
else 
	echo "$str_3 is zero length"
fi
