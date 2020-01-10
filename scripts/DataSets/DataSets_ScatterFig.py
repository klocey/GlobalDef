from __future__ import division
import numpy as np
from os.path import expanduser
import scipy.stats as sc
import sys
import pandas as pd
from math import pi
import matplotlib.pyplot as plt
from random import randint
from pylab import *

mydir = expanduser("~/GitHub/GlobalDef")
df = pd.read_csv(mydir+'/DataSets/DataSets.txt')
df = df[df['distance'] > 0]
df = df[df['name'] != 'global']
df = df[df['name'] != 'water']
df = df[df['name'] != 'hemi']
df = df[df['name'] != 'land']


def randcolor():
    c1 = randint(0,255)
    c2 = randint(0,255)
    c3 = randint(0,255)

    clr = '#%02x%02x%02x' % (c1, c2, c3)
    return clr


namesDF = list(set(df['name']))

names = []
mean = []
var = []
skew = []
mainDs = []
clrs = []
for name in namesDF:
    
    names.append(name)
    ds = df[df['name'] == name]
    ds = ds['distance']
    mainDs.append(ds)
    mean.append(np.mean(ds))
    var.append(np.var(ds))
    skew.append(sc.skew(ds))
    clr = randcolor()
    clrs.append(clr)



fig = plt.figure(figsize=(12, 12))
rc('axes', linewidth=2)

fs = 14
pt_sz = 90
a_val = 0.5
hline_clr = '0.7'
mean, skew, var, mainDs, names = zip(*sorted(zip(mean, skew, var, mainDs, names)))

ax = fig.add_subplot(311)
plt.scatter(range(len(mean)), mean, c=clrs, s=pt_sz, linewidths=0.0, edgecolors=None)
plt.axhline(10007.614102966581, 0, 100, color=hline_clr, linewidth=2, ls='--')
for i, m in enumerate(range(len(names))):
    plt.axvline(m, 0, 100000, c=clrs[i], linewidth=1, ls='--', alpha=a_val)
plt.tick_params(axis='x', bottom='off', labelbottom='off')
plt.ylabel('Mean distance', fontsize=fs+4)
plt.yticks(fontsize=fs-2)


ax = fig.add_subplot(312)
plt.scatter(range(len(var)), var, c=clrs, s=pt_sz, linewidths=0.0, edgecolors=None)
plt.axhline(19010579.645256173, 0, 100, color=hline_clr, linewidth=2, ls='--')
for i, m in enumerate(range(len(names))):
    plt.axvline(m, 0, 100000, c=clrs[i], linewidth=1, ls='--', alpha=a_val)
plt.tick_params(axis='x', bottom='off', labelbottom='off')
plt.ylabel('Variance', fontsize=fs+4)
plt.yscale('log')
plt.yticks(fontsize=fs-2)


ax = fig.add_subplot(313)
plt.scatter(range(len(skew)), skew, c=clrs, s=pt_sz, linewidths=0.0, edgecolors=None)
plt.axhline(0.0, 0, 100, color=hline_clr, linewidth=2, ls='--')
for i, m in enumerate(range(len(names))):
    plt.axvline(m, 0, 100000, c=clrs[i], linewidth=1, ls='--', alpha=a_val)
x1 = range(len(names))

plt.ylabel('Skewness', fontsize=fs+4)
plt.yticks(fontsize=fs-2)
plt.xticks(x1, names, rotation=75, fontsize=fs-2)

plt.subplots_adjust(wspace=0.0, hspace=0.0)
plt.savefig(mydir+'/figures/Fig3_Scatter.png', dpi=400, bbox_inches = "tight")
plt.close()