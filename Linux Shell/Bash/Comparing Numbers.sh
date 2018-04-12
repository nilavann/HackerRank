#!/bin/python3

read num1
read num2

# use (()) 
# comment script use :''
: '
if (($num1 == $num2)); then
    echo "X is equal to Y"
elif (($num1 < $num2)); then
    echo "X is less than Y"
else
    echo "X is greater than Y"
fi
'

# using -eq -lt -gt

if [ $num1 -gt $num2 ]; then
    echo "X is greater than Y"
elif [ $num1 -eq $num2 ]
then
    echo "X is equal to Y"
else
    echo "X is less than Y"
fi