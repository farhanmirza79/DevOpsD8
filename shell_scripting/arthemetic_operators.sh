#!/bin/bash
#Author:Farhan
#Arthemetic operators in linux


a=10
b=20

#Addition

val=`expr $a + $b`
echo "The sum of $a and $b is: $val"

#Subtraction
val=`expr $a - $b`
echo " The difference of $a and $b is: $val"

#Multiplication
val=`expr $a \* $b`
echo "The multiplication of $a and $b is: $val"

#Division
val=`expr $b / $a`
echo "The division of $b and $a is: $val"

#Modulus
val=`expr $b % $a`
echo "The modulus of $b and $a is: $val"

#Equality operator and if..else..fi conditionals

if [ $a == $b ]; then 
	echo "$a is equal to $b"
else
	echo "$a is not equal to $b"
fi 



