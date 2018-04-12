#!/bin/python3

read num1
read num2

# In bash $(()) is preparable

echo "$(($num1+$num2))"
echo "$(($num1-$num2))"
echo "$(($num1*$num2))"
echo "$(($num1/$num2))"

# we use echo `expr $num1 + $num2` instead