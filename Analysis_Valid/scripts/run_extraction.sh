#!/bin/bash
#
# (re)-)extract data from .pkl files
# [20200902] (air@cmu.edu)
# -- run this from the repository root (./scripts/run_...)
#

if [[ $# -ne 2 ]] ; then
    echo "usage: $0 <file_path.pkl> <result_file>"; exit ; fi

dest=$2
if [ ! -d $dest ] ; then
    echo "creating ${dest}/"
    mkdir $dest
fi


pkl=$1
if [[ "${pkl##*.}" == "pkl" ]]; then  # check extension
    python3 scripts/pkl_process.py $pkl $dest  # run from the origin
else
    echo "first file must be a .pkl"; exit ; fi

#
