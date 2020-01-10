from __future__ import division
import cartopy.crs as ccrs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from os.path import expanduser
from scipy.stats.kde import gaussian_kde

from math import pi
import sys
mydir = expanduser("~/GitHub/GlobalDef")
sys.path.append(mydir+"/scripts")
import fxns


#df = pd.read_csv(mydir + '/SimData/PermTest-great_circle.txt')
#print(len(df['sim']))
#sys.exit()


def get_kdens_choose_kernel(_list,kernel):
    """ Finds the kernel density function across a sample of SADs """
    density = gaussian_kde(_list)
    n = len(_list)
    #xs = np.linspace(0, 1, n)
    xs = np.linspace(min(_list), max(_list), n)
    density.covariance_factor = lambda : kernel
    density._compute_covariance()
    D = [xs,density(xs)]
    return D


def hulls(x,y):
    grain_p = 10 
    clim_p = 95
    xran = np.arange(min(x), max(x), grain_p).tolist()
    binned = np.digitize(x, xran).tolist()
    bins = [list([]) for _ in range(len(xran))]
    
    for ii, val in enumerate(binned):
        bins[val-1].append(y[ii])
    
    pct5 = []
    pct95 = []
    xran2 = []
    
    for iii, _bin in enumerate(bins):
        if len(_bin) > 0:
            clim = clim_p
            pct5.append(np.percentile(_bin, 100 - clim))
            pct95.append(np.percentile(_bin, clim))
            xran2.append(xran[iii])
    
    return xran2, pct5, pct95


ortho = ccrs.Orthographic(central_longitude=0, central_latitude=20)
geo = ccrs.Geodetic()


ed = pi*6371
S = 10**5
lw = 1
sz = 0.1
clr1 = 'm'
clr2 = 'k'
fs = 16

alpha_p = 1.0 
lw_p = 0.5
hlin = 0.5

rows = 4
cols = 12

lats = []
lons = []
loc1 = [-90, 0]    
method = 'great_circle'
kind = 'global'

ct = 1
lons_lats = fxns.get_pts(S, loc1, ed, method)

for lon_lat in lons_lats:
    lons.append(lon_lat[0])
    lats.append(lon_lat[1])

lonlats = [[0,0], [0,90], [0,-90], [-180, 0]]

fig = plt.figure(figsize=(12, 12))

ortho = ccrs.Orthographic(central_longitude=0, central_latitude=0)
m = plt.subplot2grid((rows, cols), (0, 0), colspan=3, rowspan=1, projection=ortho)
m.scatter(lons, lats, marker='o',color=clr1,s=sz, linewidths=0.0, transform=geo)
m.set_global()
m.coastlines(linewidth=lw)
plt.title('A', fontsize=fs)


ortho = ccrs.Orthographic(central_longitude=-180, central_latitude=0)
m = plt.subplot2grid((rows, cols), (0, 3), colspan=3, rowspan=1, projection=ortho)
m.scatter(lons, lats, marker='o',color=clr1,s=sz, linewidths=0.0, transform=geo)
m.set_global()
m.coastlines(linewidth=lw)
plt.title('B', fontsize=fs)

ortho = ccrs.Orthographic(central_longitude=0, central_latitude=90)
m = plt.subplot2grid((rows, cols), (0, 6), colspan=3, rowspan=1, projection=ortho)
m.scatter(lons, lats, marker='o',color=clr1,s=sz, linewidths=0.0, transform=geo)
m.set_global()
m.coastlines(linewidth=lw)
plt.title('C', fontsize=fs)

ortho = ccrs.Orthographic(central_longitude=0, central_latitude=-90)
m = plt.subplot2grid((rows, cols), (0, 9), colspan=3, rowspan=1, projection=ortho)
m.scatter(lons, lats, marker='o',color=clr1,s=sz, linewidths=0.0, transform=geo)
m.set_global()
m.coastlines(linewidth=lw)
plt.title('D', fontsize=fs)



df = pd.read_csv(mydir + '/SimData/PermTest-'+method+'.txt')

sims = list(set(df['sim']))

m = plt.subplot2grid((rows, cols), (1, 0), colspan=4, rowspan=1) 
kernel = 0.5
x2 =df['var1'].tolist()
D = get_kdens_choose_kernel(x2, kernel)
plt.plot(D[0],D[1],color = clr1, lw=2, alpha = 0.99, label= 'Random walk algorithm')
x2 =df['var2'].tolist()
D = get_kdens_choose_kernel(x2, kernel)
plt.plot(D[0],D[1],color = clr2, lw=2, ls='--', alpha = 0.99, label= 'Discrete uniform distribution')

plt.legend(bbox_to_anchor=(-0.04, 1.02, 3.16, .2), loc=10, ncol=2, mode="expand",prop={'size':fs-2})

plt.tick_params(axis='both', labelsize=fs-6)
plt.xlabel('Variance', fontsize=16)
plt.ylabel('Density', fontsize=16)
m.axes.get_yaxis().set_visible(False)
plt.text(-350, 0.0004, 'Density', rotation='90', fontsize=fs)

m = plt.subplot2grid((rows, cols), (1, 4), colspan=4, rowspan=1) 
x2 =df['skew1'].tolist()
D = get_kdens_choose_kernel(x2, kernel)
plt.plot(D[0],D[1],color = clr1, lw=2, alpha = 0.99)
x2 =df['skew2'].tolist()
D = get_kdens_choose_kernel(x2, kernel)
plt.plot(D[0],D[1],color = clr2, ls='--', lw=2, alpha = 0.99)

plt.tick_params(axis='both', labelsize=fs-6)
plt.xlabel('Skewness', fontsize=16)
m.axes.get_yaxis().set_visible(False)

m = plt.subplot2grid((rows, cols), (1, 8), colspan=4, rowspan=1) 
kernel = 0.5
x2 =df['kur1'].tolist()
D = get_kdens_choose_kernel(x2, kernel)
plt.plot(D[0],D[1],color = clr1, lw=2, alpha = 0.99)
x2 =df['kur2'].tolist()
D = get_kdens_choose_kernel(x2, kernel)
plt.plot(D[0],D[1],color = clr2, ls='--', lw=2, alpha = 0.99)
    
plt.tick_params(axis='both', labelsize=fs-6)
plt.xlabel('Kurtosis', fontsize=16)
m.axes.get_yaxis().set_visible(False)


plt.subplots_adjust(wspace=0.2, hspace=0.25)
plt.savefig(mydir+'/figures/Fig1.png', dpi=400, bbox_inches = "tight")
plt.close()