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



land_shp_fname = shpreader.natural_earth(resolution='10m', 
    category='physical', name='land')
        
land_geom = unary_union([record.geometry
    for record in shpreader.Reader(land_shp_fname).records()
    if record.attributes.get('featurecla') != "Null island"])

land = prep(land_geom)


        
outstring = 'name,distance'
OUT = open(mydir + '/DataSets/Distances/DataSets.txt', 'w+')
OUT.write(outstring+'\n')
OUT.close()



names = ['JFish', 'ROM', 'Mosquito', 'UofVienna', 'SAIAB', 'CMHerps',
         'CONN', 'Arctic', 'WTU', 'LACM', 'Geneva', 'CMBird', 'Macaulay', 
         'Eumyceto', 'AMNH-M', 'Edaphobase', 'TexAM', 'MAL', 'OSUC', 'Neptune',
         'UCFC', 'AMNH-B', 'IllNat', 'UPS', 'FishBase', 'BPBM', 'MICROBIS',
         'RoyBot', 'PRECIS', 'Hatikka', 'SAFRING', 'ZOBODAT', 'SAHFOS',
         'PaleoB', 'PlutoF']


for name in names:
    
    OUT = open(mydir + '/DataSets/Distances/DataSets.txt', 'a+')
    
    try:
        df = pd.read_csv(mydir + '/DataSets/GBIF/'+name+'/'+name+'.csv', sep='\t')
    
    except: 
        continue

    dflons = df['decimalLongitude'].tolist()
    dflats = df['decimalLatitude'].tolist()
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
    
        outlist = [name, D]
        outlist = str(outlist).strip('[]')
        outlist = outlist.replace("'", "")
        outlist = outlist.replace(" ", "")
        OUT.write(outlist+'\n')

        print(i, name)
        
    OUT.close()



ir = 2*10**3
loc1 = [90,0]
ed = pi*float(6371.0087714150598)

kinds = ['global', 'hemi', 'land', 'water']
for kind in kinds:
    
    OUT = open(mydir + '/DataSets/Distances/DataSets.txt', 'a+')
    
    method = 'great_circle'
    lons_lats = fxns.get_pts(ir, loc1, ed, method, kind, land)
    
    lons = []
    lats = []
    for i in lons_lats:
        lons.append(i[0])
        lats.append(i[1])
        
    Ds = []
    for i in range(ir):
        for j in range(i, ir):
            
            lon1 = lons[i]
            lat1 = lats[i]
            
            lon2 = lons[j]
            lat2 = lats[j]
            
            D = fxns.haversine(lon1, lat1, lon2, lat2)
            
            outlist = [kind, D]
            outlist = str(outlist).strip('[]')
            outlist = outlist.replace("'", "")
            outlist = outlist.replace(" ", "")
            OUT.write(outlist+'\n')

            print(i, kind)
        
    OUT.close()
