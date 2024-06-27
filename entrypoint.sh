#!/bin/sh -l
# First argument is the path to the source file.
# Optional -o argument is the path to the output file.
# 
# If -o is omitted, the output will be written to STDOUT
python3 ref-links-to-inline.py $1 -o $2
