from __future__ import division
import numpy as np
from os.path import expanduser
import scipy.stats as sc
import sys
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
from random import randint


mydir = expanduser("~/GitHub/GlobalDef")
df = pd.read_csv('DataSets.txt')
df = df[df['distance'] > 0]


def randcolor():
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)

    clr = '#%02x%02x%02x' % (c1, c2, c3)
    return clr



names1 = ['GBI', 'MCDB', 'EMP', 'global', 'Neptune', 'water', 'Mosquito', 'AMNH-M', 
          'MICROBIS', 'hemi', 'land', 'Geneva', 'Macaulay', 'Eumyceto', 'RoyBot', 
          'ROM', 'PaleoB', 'OSUC', 'JFish', 'FishBase', 'LACM', 'UPS', 'CMBird']

names2 = ['UofVienna', 'Africa', 'CASzoo', 'CMHerps', 'CONN', 'Arctic', 'WTU',
         'Edaph', 'TexAM', 'MAL', 'UCFC', 'AMNH-B', 'IllNat', 'BPBM',
         'PRECIS', 'Hatikka', 'SAFRING', 'giezen', 'Plank', 'PlutoF']


namesDF = list(set(df['name']))


names = []
mean = []
var = []
skew = []
mainDs = []
for name in namesDF:
    if name in names1:
        names.append(name)
        ds = df[df['name'] == name]
        ds = ds['distance']
        mainDs.append(ds)
        mean.append(np.mean(ds))
        var.append(np.var(ds))
        skew.append(sc.skew(ds))

mean, skew, var, mainDs, names = zip(*sorted(zip(mean, skew, var, mainDs, names)))

fig = plt.figure(figsize=(12, 12)) 
ax = fig.add_subplot(221)

red_square = dict(markerfacecolor='k', marker='.', markersize=0.5)
bp = ax.boxplot(mainDs, vert=0, labels=names, showfliers=False, 
                flierprops=red_square, patch_artist=True)

clrs = []
for i in range(len(bp['boxes'])):
    clr = randcolor()
    clrs.append(clr)


for i, box in enumerate(bp['boxes']):
    # change outline color
    box.set(facecolor= 'w', color=clrs[i], linewidth=1, alpha=0.4)

## change color and linewidth of the medians
for i, median in enumerate(bp['medians']):
    median.set(color=clrs[i], linewidth=2)
    
clrs2 = []
for i in clrs:
    clrs2.extend([i,i])
    
## change color and linewidth of the whiskers
for i, whisker in enumerate(bp['whiskers']):
    whisker.set(color=clrs2[i], linewidth=1)

## change color and linewidth of the caps
for i, cap in enumerate(bp['caps']):
    cap.set(color=clrs2[i], linewidth=1)

plt.axvline(10007.5, 0, 100, color='k', linewidth=1, ls='--')
plt.xlim(-150,20050)








ax = fig.add_subplot(222)

names = []
mean = []
var = []
skew = []
mainDs = []
for name in namesDF:
    if name in names2:
        names.append(name)
        ds = df[df['name'] == name]
        ds = ds['distance']
        mainDs.append(ds)
        mean.append(np.mean(ds))
        var.append(np.var(ds))
        skew.append(sc.skew(ds))
    
mean, skew, var, mainDs, names = zip(*sorted(zip(mean, skew, var, mainDs, names)))

red_square = dict(markerfacecolor='k', marker='.', markersize=0.5)
bp = ax.boxplot(mainDs, vert=0, labels=names, showfliers=True, 
                flierprops=red_square, patch_artist=True)


clrs = []
for i in range(len(bp['boxes'])):
    clr = randcolor()
    clrs.append(clr)


for i, box in enumerate(bp['boxes']):
    # change outline color
    box.set(facecolor= 'w', color=clrs[i], linewidth=1, alpha=0.4)

## change color and linewidth of the medians
for i, median in enumerate(bp['medians']):
    median.set(color=clrs[i], linewidth=2)
    
clrs2 = []
for i in clrs:
    clrs2.extend([i,i])
    
## change color and linewidth of the whiskers
for i, whisker in enumerate(bp['whiskers']):
    whisker.set(color=clrs2[i], linewidth=1)

## change color and linewidth of the caps
for i, cap in enumerate(bp['caps']):
    cap.set(color=clrs2[i], linewidth=1)


plt.axvline(10007.5, 0, 100, color='k', linewidth=1, ls='--')
plt.xlim(-150,20050)


plt.savefig(mydir+'/figures/Fig3.png', dpi=400, bbox_inches = "tight")
plt.close()