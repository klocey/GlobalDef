from __future__ import division
import numpy as np
from os.path import expanduser
import scipy.stats as sc
import sys
import pandas as pd
from math import pi

import cartopy.io.shapereader as shpreader
from shapely.ops import unary_union
from shapely.prepared import prep

mydir = expanduser("~/GitHub/GlobalDef")
sys.path.append(mydir+"/scripts")
import fxns


name = 'AMNH-B'
fname = mydir + '/DataSets/GBIF/'+name+'/'+name+'.csv'
with open(fname, "r") as infile:
    lines = infile.readlines()


print(len(lines))
data = []
for line in lines:
    line = line.split("\t")
    if len(line) == 50:
        data.append(line)
print(len(data))    

df = pd.DataFrame(data[1:], columns=data[0])
print(list(df))


names = ['AMNH-B']
for name in names:
    
    OUT = open(mydir + '/DataSets/Distances/DataSets-'+name+'.txt', 'a+')
    
    dflons = df['decimalLongitude'].tolist()
    dflats = df['decimalLatitude'].tolist()
    
    lons = []
    lats = []
    
    for i, lon in enumerate(dflons):
        lat = dflats[i]
        if lon != "" and lat != "" and lon != " " and lat != " ":
            lon = eval(lon)
            lat = eval(lat)
            if np.isnan(lon) == False and np.isnan(lat) == False:
                lons.append(lon)
                lats.append(lat)
    
    print(name,' : ',min(lons),max(lons),min(lats),max(lats))
    print(len(lons), len(lats))
    
    #sys.exit()
    
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
    
        outlist = [name, D]
        outlist = str(outlist).strip('[]')
        outlist = outlist.replace("'", "")
        outlist = outlist.replace(" ", "")
        OUT.write(outlist+'\n')

        print(i, name)
        
    OUT.close()