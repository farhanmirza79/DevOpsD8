#!/bin/bash
#Author : Mirza Farhan
#This script explains about local vars


getName(){
NAME="Farhan"   #local variable
echo "$NAME - from inside the function"
}

echo "$NAME - outside the funciton"
getName
echo "$NAME - outside the function after calling the fucntion"



AGE=100 #Global Variable

getAge(){
echo "My age is : $AGE - Inside the function"
}

echo "My age is : $AGE - Outside the function" 
getAge
