from __future__ import division
import numpy as np
from os.path import expanduser
import scipy.stats as sc
import sys
import pandas as pd
from math import pi

mydir = expanduser("~/GitHub/GlobalDef")
sys.path.append(mydir+"/scripts")
import fxns


outstring = 'name,distance'
OUT = open(mydir + '/DataSets/Distances/DataSets-GloBI.txt', 'w+')
OUT.write(outstring+'\n')
OUT.close()

OUT = open(mydir + '/DataSets/Distances/DataSets-GloBI.txt', 'a+')


name = 'GloBI'
df = pd.read_csv(mydir + '/DataSets/GloBI/GloBI/interactions_latlons.txt', sep='\t')


col_headers = list(df)
for c in col_headers:
    print(c)


dflons = df['decimalLongitude'].tolist()
dflats = df['decimalLatitude'].tolist()
df = int(0)
print(len(dflons), len(dflats))


ct1 = 0
ct2 = 0
for lat in dflats:
    if lat > -90 and lat < 90:
        ct1 += 1
    if lat > 0 and lat <= 90:
        ct2 += 1

print(name, 'num sites:', len(dflons), 
      'sites with coords:', ct1,
      'portion of sites in N. hemisphere', ct2/ct1)


lons = []
lats = []
    
for i, lon in enumerate(dflons):
    lat = dflats[i]
    if np.isnan(lon) == False and np.isnan(lat) == False:
        lons.append(lon)
        lats.append(lat)
    
print(name,' : ',min(lons),max(lons),min(lats),max(lats), '  ',len(lons), len(lats))
    

Is = range(len(lons))
    
for i in range(100000):
    i1, i2 = np.random.choice(Is, size=2, replace=False)

    lon1 = lons[i1]
    lat1 = lats[i1]
        
    lon2 = lons[i2]
    lat2 = lats[i2]
    
    if lon1 < -180 or lon1 > 180: continue
    if lon2 < -180 or lon2 > 180: continue
    if lat1 < -90 or lat1 > 90: continue
    if lat2 < -90 or lat2 > 90: continue
            
    D = fxns.haversine(lon1, lat1, lon2, lat2)
    if D == 0: continue

    outlist = [name, D]
    outlist = str(outlist).strip('[]')
    outlist = outlist.replace("'", "")
    outlist = outlist.replace(" ", "")
    OUT.write(outlist+'\n')

    print(i, name)
        
OUT.close()