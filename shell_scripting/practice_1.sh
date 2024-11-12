#!/bin/bash

# Step 1: Create an array with different data types
my_array=(10 "Hello" 3.14 true "None")

# Step 2: Change the value at the 2nd index (third element)
my_array[2]="New Value"

# Step 3: Print all the values of the array together using a special variable
echo "${my_array[@]}"


















