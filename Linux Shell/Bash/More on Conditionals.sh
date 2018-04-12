#!/bin/bash

read num1
read num2
read num3

if [ $num1 -eq $num2 -a $num2 -eq $num3 -a $num1 -eq $num3 ]; then
    echo "EQUILATERAL"
elif [ $num1 -ne $num2 -a $num2 -ne $num3 -a $num1 -ne $num3 ]; then
    echo "SCALENE"
else
    echo "ISOSCELES"
fi