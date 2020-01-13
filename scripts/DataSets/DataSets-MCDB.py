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
OUT = open(mydir + '/DataSets/Distances/DataSets-MCDB.txt', 'w+')
OUT.write(outstring+'\n')
OUT.close()


OUT = open(mydir + '/DataSets/Distances/DataSets-MCDB.txt', 'a+')


name = 'MCDB'
df = pd.read_csv(mydir + '/DataSets/MCDB/MCDB_latlon.csv', sep=',')

dflons = df['Longitude'].tolist()
dflats = df['Latitude'].tolist()
lons = []
lats = []

df2 = df[df['Latitude'] > 0.0]['Latitude']
print(len(df2))
print(name, len(dflons))



for i, lon in enumerate(dflons):
    lat = dflats[i]
    if np.isnan(lon) == False and np.isnan(lat) == False:
        lons.append(lon)
        lats.append(lat)
    
print(name,' : ',min(lons),max(lons),min(lats),max(lats))

    

Is = range(len(lons))
    
for i in range(10000):
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
