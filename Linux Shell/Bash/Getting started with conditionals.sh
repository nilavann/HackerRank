#!/bin/bash

read character

if [ $character = "Y" -o $character = "y" ]; then
    echo "YES"
else
    echo "NO"
fi