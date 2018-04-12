#!/bin/bash

read n
sum=0
for ((i=0;i<$n;i++))
    do
        read num
        sum=$(($sum+$num))
    done
# echo $sum 
printf "%.3f" $(echo $sum/$n | bc -l)