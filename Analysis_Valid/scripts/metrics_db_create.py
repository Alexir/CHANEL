#!/usr/bin/env python
# 
# [20201014] (air) create a sqlite db for Metrics/Validity
#

import sys, os, argparse
import csv
from pprint import pprint
import sqlite3
import csv
#



#if __name__ == 'main' :
if True :
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataf','-da', type=str, help='source file for Metrics/Validity item data',required=True)
    parser.add_argument('--sqlf','-sq', type=str, help='sql definition for data table',required=True)
    parser.add_argument('--db','-db', type=str, help='database file of Metrics/Validity item data',required=True)
    parser.add_argument('--table','-tab', type=str, help='into which table to put data (defn in sqlf!)',required=True)
    
    args = parser.parse_args()
    conn = sqlite3.connect(args.db)
    curs = conn.cursor()
    
    # set up the schema; this will recreate the db from source
    with open(args.sqlf,'r') as fp : table_def = fp.readlines()
    curs.executescript(''.join(table_def))
    conn.commit()
    
    # read .csv lines; store in db
    #curs.execute('BEGIN TRANSACTION')  # suspend autocommit (for speed)
    with open(args.dataf,'r') as csvf:
        items = csv.reader(csvf)
        col_cnt = 1
        if ( csv.Sniffer().has_header ) :
            HAS_HEADER = True
            cols = items.__next__()  # lop off the column headers
            delim = csv.Sniffer().sniff(cols[0])
            col_cnt = len( cols[0].split(delim.delimiter) )
            print('cnt:',col_cnt,'\t',cols[0])

        sql = 'INSERT INTO '+args.table+' VALUES( ' + '?,'*(col_cnt-1)+ '? )'
        print(sql)
        cnt = 0
        # hit dada: [0]:UID item id  [1]:SID speaker#  [2]:SEG text of turn
        for row in items :
            row = row[0].split(delim.delimiter)
            # print(row)
            curs.execute(sql,row)
            cnt +=1

    #curs.execute('COMMIT TRANSACTION')  # resume autocommit, commit

    conn.commit()
    curs.close()
    
#











#
