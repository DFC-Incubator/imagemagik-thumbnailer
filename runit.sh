#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

echo "arg0 $1"
echo "arg1 $2"

python /make_thumbs_with_imagemagick.py -f $1 -w $2

