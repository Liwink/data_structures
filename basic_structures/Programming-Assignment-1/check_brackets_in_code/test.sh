#!/bin/bash

for i in {1..53}
do
    if [ $i -lt 10 ]
    then
        python check_brackets.py < "tests/0$i"
        cat "tests/0$i.a"
    else
        python check_brackets.py < "tests/$i"
        cat "tests/$i.a"
    fi
    echo ""
done
