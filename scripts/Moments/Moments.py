from __future__ import division
import numpy as np
from os.path import expanduser
from math import pi
import scipy.stats as sc
import sys
from geopy.distance import geodesic
import scipy.special

from timeit import default_timer as timer

import cartopy.io.shapereader as shpreader
from shapely.ops import unary_union
from shapely.prepared import prep

mydir = expanduser("~/GitHub/GlobalDef")
sys.path.append(mydir+"/scripts")
import fxns


OUT = open(mydir + '/SimData/Moments.txt', 'w+')
outstring = 'sites,sim,method,type,mean,var,skew'
OUT.write(outstring+'\n')


loc1 = [90,0]
ed = pi*float(6371.0087714150598) # 1/2 of Earth's GCD-based circumference

method = 'great_circle'

mean = []
var = []
skew = []

num_sites = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
             200, 300, 400, 500, 600, 700, 800, 900, 1000]

kinds = ['global', 'hemi', 'land', 'water']
for kind in kinds:
    
    land = 'none'
    if kind == 'land' or kind == 'water':
        land_shp_fname = shpreader.natural_earth(resolution='10m', 
            category='physical', name='land')
        
        land_geom = unary_union([record.geometry
            for record in shpreader.Reader(land_shp_fname).records()
            if record.attributes.get('featurecla') != "Null island"])
        
        land = prep(land_geom)
        
    for sites in num_sites:
        for sim in range(1000):
                
            lons_lats = fxns.get_pts(sites, loc1, ed, method, kind, land)
            
            Ds = []
            lats = []
            lons = []
                    
            for lon_lat in lons_lats:
                lons.append(lon_lat[0])
                lats.append(lon_lat[1])
                    
            ss = scipy.special.comb(sites, 2, exact=True)
            
            start = timer()
            for i in range(len(lons)):
                for j in range(len(lons)):
                    if j <= i: continue
                
                    lon1 = lons[i]
                    lat1 = lats[i]
                    lon2 = lons[j]
                    lat2 = lats[j]
                        
                    if method == 'great_circle':
                        D = fxns.haversine(lon1, lat1, lon2, lat2)
                    elif method == 'geodesic':
                        D = geodesic([lat1, lon1], [lat2, lon2]).kilometers
                            
                    Ds.append(D)
            
            #print(ss, len(Ds))
            end = timer()
            t = end-start
            
            mean = np.mean(Ds)
            var = np.var(Ds)
            skew = sc.skew(Ds)
            
            print(sites, sim, method, kind,' | mean:', round(mean,4), 'var:', 
                  round(var,4), 'skew:', round(skew,4), 'time:', round(t,4))
        
            outlist = [sites, sim, method, kind, mean, var, skew]
            outlist = str(outlist).strip('[]')
            outlist = outlist.replace(" ", "")
            
            OUT = open(mydir + '/SimData/Moments.txt', 'a+')
            OUT.write(outlist+'\n')
            OUT.close()