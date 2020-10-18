#!/use5bin/env python
#
# [2021018] (air) add a duration column to Session table
#

import sys, os, argparse
import csv
from pprint import pprint
from datetime import datetime
import time
import csv
#

if True :
    parser = argparse.ArgumentParser()
    parser.add_argument('--sess','-se', type=str, help='Session file for Metrics/Validity item data',required=True)
    parser.add_argument('--dursess','-du', type=str, help='Session file + session duration',required=True)
    args= parser.parse_args()

    with open(args.sess,'r') as csvf, open(args.dursess,"w") as outf :
        items = csv.reader(csvf)
        col_cnt = 1
        if ( csv.Sniffer().has_header ) :
            HAS_HEADER = True
            cols = items.__next__()  # lop off the column headers
            delim = csv.Sniffer().sniff(cols[0])
            header = cols[0].split(delim.delimiter) 
            col_cnt = len( header )
            print('cnt:',col_cnt,'\t',header[0])

            Accept = header.index('AcceptTime')
            Submit = header.index('SubmitTime')
            header.insert(Submit+1,str('Duration'))
            outf.write('\t'.join(header) +'\n')
            for row in items :
            
                dt_format = "%Y-%m-%d %H:%M:%S"
                row = row[0].split(delim.delimiter)
                Duration = datetime.strptime(row[Submit],dt_format) - datetime.strptime(row[Accept],dt_format)
                row.insert(Submit+1,str(Duration))
                outf.write('\t'.join(row) +'\n')

                


#
