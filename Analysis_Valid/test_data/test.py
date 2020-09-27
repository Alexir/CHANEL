#
# play with pivots
#

import sys,os
from pprint import pprint
import numpy as np
import pandas as pd
import math

import krippendorff as kripp

import nltk
from nltk.metrics.agreement import AnnotationTask
from nltk.metrics.distance  import *

# get the base validition data
import py_module_krippendorff as pykri
    
print('reliability_data')
pprint(pykri.reliability_data)
print('nominal  [0.691]:',
      round(kripp.alpha(pykri.reliability_data, level_of_measurement='nominal'),3))
print('ordinal  [     ]:',
      round(kripp.alpha(pykri.reliability_data, level_of_measurement='ordinal'),3))
print('interval [0.811]:',
      round(kripp.alpha(pykri.reliability_data, level_of_measurement='interval'),3))
print()

print('reliability_data_2')
pprint(pykri.reliability_data_2)
print('nominal [     ]:',
      round(kripp.alpha(pykri.reliability_data_2, level_of_measurement='nominal'),3))
print('ordinal [0.815]:',
      round(kripp.alpha(pykri.reliability_data_2, level_of_measurement='ordinal'),3))
print('ratio   [0.797]: ',
      round(kripp.alpha(pykri.reliability_data_2, level_of_measurement='ratio'),3))
print()


with open('artstein_poesio_example.txt','r') as fp :

    # -- column names are for (my) convenience
    dat = pd.read_csv(fp,names=['c','i','k'],delimiter='\t')

    print("artstein_poesio original:\n",dat)
    
    # make k column numeric (turn strs into numbers)
    labels = pd.unique(dat['k'])  # set or reponse labers
    zz = {}
    zzz = zip(labels,np.arange(len(labels)))
    for z in zzz : zz[z[0]] = z[1]  # create an arbitrary dic mapping to numbers

    # numeralize the str responses
    dat['k'] = dat['k'].apply(lambda x : zz[x] )
    
    piv = dat.pivot(columns='i', index='c', values='k')
    # piv = piv.fillna(np.nan)  # get the right NaN in there
    # print("pivoted:\n",piv,'\n')

    # now try on a&p data
    print('artstein & poesio data:')
    piv = piv.values  # conform to alpha()
    print('nominal:  ', round(kripp.alpha(piv,  level_of_measurement='nominal'),3))
    print('interval: ',round( kripp.alpha(piv, level_of_measurement='interval'),3))
    print('ordinal: ',round( kripp.alpha(piv, level_of_measurement='ordinal'),3))
    print()

    print ('\ntry this with nltk')
    # ------------------
    t_binary = AnnotationTask( data=dat.values, distance=binary_distance )
    t_interval = AnnotationTask(data=dat.values,distance=interval_distance)

    # mean observed agreement across all coders and items.
    print(" avg_Ao:    ",round(t_binary.avg_Ao(),3),round(t_interval.avg_Ao(),3) )
    
    # Bennett, Albert and Goldstein 1954
    print("     pi:    ",round(t_binary.pi(),3), round(t_interval.pi(),3) )
    
    # Scott 1955; here, multi-pi.
    print("      S:    ",round(t_binary.S(),3),round(t_interval.S(),3) )
    print()
    # Cohen 1960 Averages naively over kappas for each coder pair.
    print("      kappa:",round(t_binary.kappa(),3),round(t_interval.kappa(),3) )
    # Davies and Fleiss 1982 Averages over observed and expected agreements for each coder pair.
    print("multi_kappa:",round(t_binary.multi_kappa(),3),round(t_interval.multi_kappa(),3) )
    print()
    
    print("binary   alpha:",round(t_binary.alpha(),3))    # krippendorff
    print("interval alpha:",round(t_interval.alpha(),3))    # krippendorff  # nan's cause fault
    
#
