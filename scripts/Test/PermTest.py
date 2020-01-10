from __future__ import division
from os.path import expanduser
from random import choice
import numpy as np
from math import pi
import sys
import geopy
from geopy.distance import geodesic
import scipy.stats as sc
from scipy.stats import chisquare


mydir = expanduser("~/GitHub/GlobalDef")
sys.path.append(mydir+"/scripts")
import fxns



method = 'great_circle'

outstring = 'sim,iteration,num_ref_sites,dist_ref,x2,pval,x22,pval2'
outstring += ',var1,skew1,kur1,var2,skew2,kur2'
#if method == 'geodesic':
#    OUT = open(mydir + '/SimData/PermTest-geodesic.txt', 'w+')
#    OUT.write(outstring+'\n')
#else:

#OUT = open(mydir + '/SimData/PermTest-great_circle.txt', 'w+')
#OUT.write(outstring+'\n')
#OUT.close()


ed = pi*float(6371.0087714150598)
sites = 10**5

ir = 10
d_ref = 1000

for sim in range(7,10):
    
    loc1 = [90,0]
    varM1,skewM1,varM2,skewM2 = [0.0]*4
    
    if sim == 7:
        ct = 603
    else: ct = 0
    while ct < 1000:
        
        skip = 0        
        
        lats_ref = []
        lons_ref = []
        lons_lats_ref = fxns.get_pts(ir, loc1, ed, method)
        for lon_lat in lons_lats_ref:
            lon1 = lon_lat[0]
            lat1 = lon_lat[1]
                
            for lon_lat in lons_lats_ref:
                lon2 = lon_lat[0]
                lat2 = lon_lat[1]
                    
                if lat1 == lat2 and lon1 == lon2: 
                    continue
                
                dist = float()
                if method == 'great_circle':
                    dist = fxns.haversine(lon1, lat1, lon2, lat2)
                elif method == 'geodesic':
                    dist = geodesic([lat1, lon1], [lat2, lon2]).kilometers
                    
                if dist < d_ref*2: 
                    skip = 1
            
        if skip == 1: continue    
        
        lons_lats = fxns.get_pts(sites, loc1, ed, method)
        
        lats = []
        lons = []
        for lon_lat in lons_lats:
            lons.append(lon_lat[0])
            lats.append(lon_lat[1])
            
                       
        ls1 = []
        for lon_lat_ref in lons_lats_ref:
            lon1 = lon_lat_ref[0]
            lat1 = lon_lat_ref[1]
                
            num_pts = 0
                
            for lon_lat in lons_lats:
                lon2 = lon_lat[0]
                lat2 = lon_lat[1]
            
                if lat1 == lat2 and lon1 == lon2: 
                    continue
                    
                dist = float()
                if method == 'great_circle':
                    dist = fxns.haversine(lon1, lat1, lon2, lat2)
                elif method == 'geodesic':
                    dist = geodesic([lat1, lon1], [lat2, lon2]).kilometers
                
                if dist < d_ref:
                    num_pts += 1
                    
            ls1.append(num_pts)
        
        
        x2, pval = chisquare(ls1)
        
        ls2 = [0]*ir
        sum_val = sum(ls1)
        for iii in range(sum_val):
            ind = choice(range(ir))
            ls2[ind] += 1
        
        x22, pval2 = chisquare(ls2)
        
        var1 = np.var(ls1)
        skew1 = sc.skew(ls1)
        kur1 = sc.kurtosis(ls1)
                
        var2 = np.var(ls2)
        skew2 = sc.skew(ls2)  
        kur2 = sc.kurtosis(ls2)
        
        
        if skew1 == skew2 or var1 == var2: 
            continue
        
        ct += 1       
        if var1 < var2:
            varM1 += 1
            
        if skew1 < skew2:
            skewM1 += 1
            
        p1 = varM1/ct
        p2 = skewM1/ct
        

        print(sim, ct, p1, p2, pval)
            
        outlist = [sim, ct, ir, d_ref, p1, p2, x2, pval, x22, pval2, var1, skew1, kur1,
                   var2, skew2, kur2]
        
        outlist = str(outlist).strip('[]')
        outlist = outlist.replace(" ", "")
            
        
        if method == 'geodesic':
            OUT = open(mydir + '/SimData/PermTest-geodesic.txt', 'a+')
        else:
            OUT = open(mydir + '/SimData/PermTest-great_circle.txt', 'a+')
        OUT.write(outlist+'\n')
        OUT.close()
        
