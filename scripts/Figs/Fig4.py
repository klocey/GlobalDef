from __future__ import division
import cartopy.crs as ccrs

import matplotlib.pyplot as plt
import numpy as np
from os.path import expanduser


from math import pi
import sys
mydir = expanduser("~/GitHub/GlobalDef")
sys.path.append(mydir+"/scripts")
import fxns


ortho = ccrs.Orthographic(central_longitude=60, central_latitude=20)
geo = ccrs.Geodetic()

ed = pi*6371
S = 10**5
clr1 = '0.5'
clr2 = 'm'
alpha_p = 1.0
sz_p = 0.5
fs = 20

lats = [] 
lons = []
loc1 = [90,0]

method = 'great_circle'
lons_lats = fxns.get_pts(S, loc1, ed, method)
for lon_lat in lons_lats:
    lons.append(lon_lat[0])
    lats.append(lon_lat[1])



fig = plt.figure(figsize=(12, 12))   

m = plt.subplot2grid((3, 3), (0, 0), colspan=1, rowspan=1, projection=ortho)
    
lons1_all = []
lats1_all = []
lons1_sub = []
lats1_sub = []
    
for i, lat in enumerate(lats):
    if lat > 45:
        lons1_all.append(lons[i])
        lats1_all.append(lats[i])
        if lat < 55:
            lons1_sub.append(lons[i])
            lats1_sub.append(lats[i])


#print(lons1_all)
#sys.exit()
m.set_global()
m.coastlines(linewidth=1)
m.scatter(lons1_all, lats1_all, marker='o',color=clr1, s=sz_p, linewidths=0.0, alpha=alpha_p, transform=geo)
m.scatter(lons1_sub, lats1_sub, marker='o',color=clr2, s=sz_p, linewidths=0.0, alpha=alpha_p, transform=geo)
plt.title('A', fontsize=fs)


m = plt.subplot2grid((3, 3), (0, 1), colspan=1, rowspan=1, projection=ortho)
    
lons1_all = []
lats1_all = []
lons1_sub = []
lats1_sub = []
    
for i, lat in enumerate(lats):
    if lat > 0:
        lons1_all.append(lons[i])
        lats1_all.append(lats[i])
        if lat < 10:
            lons1_sub.append(lons[i])
            lats1_sub.append(lats[i])

m.scatter(lons1_all, lats1_all, marker='o',color=clr1,s=sz_p, linewidths=0.0, alpha=alpha_p, transform=geo)
m.scatter(lons1_sub, lats1_sub, marker='o',color=clr2,s=sz_p, linewidths=0.0, alpha=alpha_p, transform=geo)
m.set_global()
m.coastlines(linewidth=1)
plt.title('B', fontsize=fs)


m = plt.subplot2grid((3, 3), (0, 2), colspan=1, rowspan=1, projection=ortho)
    
lons1_all = []
lats1_all = []
lons1_sub = []
lats1_sub = []
    
for i, lat in enumerate(lats):
    if lat > -45:
        lons1_all.append(lons[i])
        lats1_all.append(lats[i])
        if lat < -35:
            lons1_sub.append(lons[i])
            lats1_sub.append(lats[i])

m.scatter(lons1_all, lats1_all, marker='o',color=clr1,s=sz_p, linewidths=0.0, alpha=alpha_p, transform=geo)
m.scatter(lons1_sub, lats1_sub, marker='o',color=clr2,s=sz_p, linewidths=0.0, alpha=alpha_p, transform=geo)
m.set_global()
m.coastlines(linewidth=1)
plt.title('C', fontsize=fs)


ax4 = plt.subplot2grid((3, 3), (1, 0), colspan=3, rowspan=1)
ax5 = ax4.twiny()

lat_cutoffs = list(range(-85, 85))
#lat_cutoffs.reverse()



lats = [] 
lons = []
loc1 = [90,0]

S = 4*10**3
method = 'great_circle'
lons_lats = fxns.get_pts(S, loc1, ed, method)
for lon_lat in lons_lats:
    lons.append(lon_lat[0])
    lats.append(lon_lat[1])
    
    
avgDs_all = []
avgDs_sub = []
num_pts = []

for cutoff in lat_cutoffs:
    print(cutoff, len(lons))
    
    lons_all = []
    lons_sub = []
    lats_all = []
    lats_sub = []
    
    for i, lat in enumerate(lats):
        if lat > cutoff:
            lats_all.append(lats[i])
            lons_all.append(lons[i])
            if lat < cutoff + 5 and lat > cutoff - 5:
                lats_sub.append(lats[i])
                lons_sub.append(lons[i])

    Ds_all = []
    Ds_sub = []
    S = len(lats_all)
    for i in range(S):
                
        lon1 = lons_all[i]
        lat1 = lats_all[i]  

        for j in range(i+1,S):
            lon2 = lons_all[j]
            lat2 = lats_all[j]           
                    
            dx = fxns.haversine(lon1, lat1, lon2, lat2)
            Ds_all.append(dx)
     
    S = len(lats_sub)
    for i in range(S):
                
        lon1 = lons_sub[i]
        lat1 = lats_sub[i]  

        for j in range(i+1,S):
            lon2 = lons_sub[j]
            lat2 = lats_sub[j]           
                    
            dx = fxns.haversine(lon1, lat1, lon2, lat2)
            Ds_sub.append(dx)
            
        
    num_pts.append(len(lons_all))
    avgD = np.mean(Ds_all)
    avgDs_all.append(avgD)
    
    avgD = np.mean(Ds_sub)
    avgDs_sub.append(avgD)

    lons = list(lons_all)
    lats = list(lats_all)


ax4.set_xlim(min(num_pts), max(num_pts))
ax4.plot(num_pts, avgDs_all, color='k', linewidth=2,alpha=alpha_p, label='All points')
ax4.plot(num_pts, avgDs_sub, color=clr2, linewidth=2,alpha=alpha_p, label='Points on leading edge')
ax4.set_xticks([0, 3*250, 3*500, 3*750, 3*1000])
ax4.set_xticklabels([0, 25000, 50000, 75000, 100000])
ax4.set_xlabel('Number of locations', fontsize=fs)
ax4.set_ylabel('Avg. distance, km', fontsize=fs)
ax4.tick_params(axis='both', labelsize=fs-4)
ax4.legend(loc=8, frameon=False, fontsize=fs-2)

ax5.set_xlabel("Latitude", fontsize=fs)
ax5.set_xticks([0, 3*250, 3*500, 3*750, 3*1000])
ax5.set_xticklabels([90, 45, 0, -45, -90])
ax5.tick_params(axis='both', labelsize=fs-4)


plt.subplots_adjust(wspace=0.15, hspace=0.35)
plt.savefig(mydir+'/figures/Fig4.png', dpi=400, bbox_inches = "tight")
plt.close()