#!/bin/bash
#
# [20201017] (air) Created
# turn as .csv file into a .db file (as defined in -sqlf)
# -- run in data folder

csv='030820_first_public-assigmt'
csva='030820_first_public-session'
tab='Session'

#python -m pdb \
       ../scripts/metrics_db_create.py \
			      -da ${csva}.csv \
			      -db ${csva}.db \
			      -ta ${tab} \
			      -sq metrics_data_schema.sql
echo 'done'

#
