#
# make a comma .csv into a tab csv
# [20200917] (air)
#

import csv, argparse
import pandas as pd


parser = argparse.ArgumentParser(description="Convert comma .csv to tab equivalent")
parser.add_argument('comma', type=str, help='comma delimited .csv')
parser.add_argument('tab', type=str, help='tab version of the comma file')
arg = parser.parse_args()

df = pd.read_csv(arg.comma, header=None)
df.drop([0,0])
df_reorder = df[[1,2,0]] # rearrange column here
df_reorder.to_csv(arg.tab, sep="\t",header=False,index=False)


"""    with open(arg.comma, 'r') as infile, open(arg.tab, 'w') as outfile:
        #comma = infile.readlines()
        for line in infile :
            outl = line.split(",")
            print(outl)
            
        stripped = (line.strip() for line in infile)
        print(stripped)
        lines = (line.split(",") for line in stripped if line)
        writer = csv.writer(outfile, delimiter='\t')
        writer.writerows(lines)
"""

#
