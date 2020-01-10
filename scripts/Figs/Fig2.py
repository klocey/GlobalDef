from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from os.path import expanduser
import sys
import pandas as pd
from math import pi

mydir = expanduser("~/GitHub/GlobalDef")
df = pd.read_csv(mydir + '/SimData/Moments.txt')
df = df[df['method'] == "'great_circle'"]    


def hulls(x,y):
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


        
######################### FIGURE 2 ########################################
alpha_p = 0.4
lw_p = 0.5
grain_p = 1 
clim_p = 95
fc = 'r'

cols = 3
rows = 3

scatter = 'n'

fs = 12
clr = 'k'
x_lab = 'Number of locations'
fig = plt.figure(figsize=(10, 10))



df2 = df[df['type'] == "'global'"]
fig.add_subplot(rows,cols,1)

x = df2['sites']
y = df2['mean'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0) 
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=0.8, lw=lw_p, label = 'Global')
plt.tick_params(axis='both', labelsize=fs-4)
v = ((pi*6371.0087714150598)/2)
plt.axhline(v, 0, 10000, linewidth=1, ls='--', c = 'k', label = 'Global expectation')



fig.add_subplot(rows,cols,2)

y = df2['var'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=0.8, lw=lw_p, label = 'Global')
plt.tick_params(axis='both', labelsize=fs-4)
v = ((6371.0087714150598)**2/(np.exp(1)*pi/4))
plt.axhline(v, 0, 10000, linewidth=1, ls='--', c = 'k', label = 'Global expectation')


fig.add_subplot(rows,cols,3)

y = df2['skew'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
plt.tick_params(axis='both', labelsize=fs-4)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=0.8, lw=lw_p, label = 'Global')
plt.axhline(0, 0, 10000, linewidth=1, ls='--', c = 'k', label = 'Global expectation')



fc = 'b'
df2 = df[df['type'] == "'water'"]
fig.add_subplot(rows,cols,1)

x = df2['sites']
y = df2['mean'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=alpha_p, lw=lw_p, label='Global aquatic')
plt.tick_params(axis='both', labelsize=fs-4)
plt.ylabel('Mean distance, km', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.legend(loc='upper right', frameon=False, fontsize=10)
plt.ylim(9000, 11000)


fig.add_subplot(rows,cols,2)

y = df2['var'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=alpha_p, lw=lw_p, label='Global aquatic')
plt.tick_params(axis='both', labelsize=fs-4)
plt.ylabel('Variance in distance', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.legend(loc='upper right', frameon=False, fontsize=10)



fig.add_subplot(rows,cols,3)

y = df2['skew'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0) 
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=alpha_p, lw=lw_p, label='Global aquatic')
plt.tick_params(axis='both', labelsize=fs-4)
plt.ylabel('Skewness of distance', fontsize=fs)
plt.legend(loc='upper right', frameon=False, fontsize=10)



fc = 'm'
df2 = df[df['type'] == "'hemi'"]
fig.add_subplot(rows,cols,4)

x = df2['sites']
y = df2['mean'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=0.8, lw=lw_p, label='Hemispheric')
plt.tick_params(axis='both', labelsize=fs-4)



fig.add_subplot(rows,cols,5)

y = df2['var'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=0.8, lw=lw_p, label='Hemispheric')
plt.tick_params(axis='both', labelsize=fs-4)



fig.add_subplot(rows,cols,6)

y = df2['skew'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0) 
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=0.8, lw=lw_p, label='Hemispheric')
plt.tick_params(axis='both', labelsize=fs-4)




fc = 'c'
df2 = df[df['type'] == "'land'"]
fig.add_subplot(rows,cols,4)

x = df2['sites']
y = df2['mean'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=alpha_p, lw=lw_p, label='Global terrestrial')
plt.tick_params(axis='both', labelsize=fs-4)
plt.ylabel('Mean distance, km', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.legend(loc='upper right', frameon=False, fontsize=10)




fig.add_subplot(rows,cols,5)

y = df2['var'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0)
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=alpha_p, lw=lw_p, label='Global terrestrial')
plt.tick_params(axis='both', labelsize=fs-4)
plt.ylabel('Variance in distance', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.legend(loc='upper right', frameon=False, fontsize=10)



fig.add_subplot(rows,cols,6)

y = df2['skew'].tolist()

if scatter == 'y':
    plt.scatter(x, y, s = 1, c = clr, linewidths=0.0) 
xran2, pct5, pct95 = hulls(x, y)
plt.fill_between(xran2, pct5, pct95, facecolor=fc, alpha=alpha_p, lw=lw_p, label='Global terrestrial')
plt.tick_params(axis='both', labelsize=fs-4)
plt.ylabel('Skewness of distance', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.legend(loc='upper right', frameon=False, fontsize=10)


plt.subplots_adjust(wspace=0.35, hspace=0.35)
#plt.savefig(mydir+'/figures/Moments_Geodesic.png', dpi=400, bbox_inches = "tight")
#plt.savefig(mydir+'/figures/Moments_GreatCircle_LandWater.png', dpi=400, bbox_inches = "tight")
plt.savefig(mydir+'/figures/Fig2.png', dpi=400, bbox_inches = "tight")
plt.close()