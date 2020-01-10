from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from os.path import expanduser
import sys
import pandas as pd


mydir = expanduser("~/GitHub/GlobalDef")

l_or_w = 'land'
df = pd.read_csv(mydir + '/SimData/MomentsSampSize_'+str(l_or_w)+'.txt')
    
        
######################### FIGURE 2 ########################################
df2 = df[df['method'] == "'great_circle'"]


num_sites = list(set(df2['num_sites'].tolist()))
num_sites.sort()

sd = 2
for n in num_sites:
    
    successes = 0
    
    df3 = df2[df2['num_sites'] == n]
    
    g_means = df3['mean'].tolist()
    g_vars = df3['var'].tolist()
    g_skews = df3['skew'].tolist()
    
    t = len(g_skews)
    for i, avg in enumerate(g_means):

        mean = 10007.151515144496
        std = 8.868724246537138
        upper = mean + std*sd
        lower = mean - std*sd
        
        if avg > lower and avg < upper:

            var = g_vars[i]    
            mean = 18977327.867391232
            std = 43903.89224906093 
            upper = mean + std*sd
            lower = mean - std*sd

            if var > lower and var < upper:
    
                skew = g_skews[i]
                mean = 0.00020418663167784087
                std = 0.002803229723684044
                upper = mean + std*sd
                lower = mean - std*sd

                if skew > lower and skew < upper:
                    successes += 1    
    
    print('sites:',n,' ','successes:',successes/t, t)

        