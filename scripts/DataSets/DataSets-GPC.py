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

def is_float(x):
    try:
        float(x)
    except ValueError:
        return False
    return True


outstring = 'name,distance'
OUT = open(mydir + '/DataSets/Distances/DataSets-GPC.txt', 'w+')
OUT.write(outstring+'\n')
OUT.close()

name = 'GPC'

OUT = open(mydir + '/DataSets/Distances/DataSets-GPC.txt', 'a+')
df = pd.read_csv(mydir + '/DataSets/GPC/GPC.tsv', sep='\t')

print(len(df['longitude']))
df = df[df['longitude'].apply(lambda x: is_float(x))]
df['longitude'] = df['longitude'].astype(float)
df = df[df['latitude'].apply(lambda x: is_float(x))]
df['latitude'] = df['latitude'].astype(float)
df = df[df['longitude'] >= -180.0]
df = df[df['longitude'] <= 180.0]
df = df[df['latitude'] >= -90.0]
df = df[df['latitude'] <= 90.0]
print(len(df['longitude']))

df2 = df[df['latitude'] > 0.0]['latitude']
print(len(df2))


dflons = df['longitude'].tolist()
dflats = df['latitude'].tolist()
lons = []
lats = []
    
for i, lon in enumerate(dflons):
    lat = dflats[i]
    if np.isnan(lon) == False and np.isnan(lat) == False:
        lons.append(lon)
        lats.append(lat)
    
print(name,' : ',min(lons),max(lons),min(lats),max(lats))
    

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
