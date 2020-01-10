from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from os.path import expanduser
#import sys
import pandas as pd


mydir = expanduser("~/GitHub/GlobalDef")
df = pd.read_csv(mydir + '/Modeling/SimData/Data4Figs.txt', sep='\t')

#print(list(df))
#print(df.iloc[15])
#sys.exit()
    
######################### FIGURE 2 ########################################
alpha_p = 0.6
lw_p = 0.5
clim_p = 75
grain_p = 600
vlin_p = 8000
xlimit = 10500

fs = 16
fig = plt.figure(figsize=(14, 12))   


fig.add_subplot(3,3,1)

typeof = 'spatial-null1'
ldg = 0
clr = '0.2'
x_lab = 'Mean distance'

df2 = df[df['latDivGrad'] == ldg]
df2 = df2[df2['model_type'] == typeof]

df3 = df2[df2['data_type'] == 'geoDs']
geoDs_main = df3['data']
df3 = df2[df2['data_type'] == 'maxDs']
maxDs_main = df3['data']
df3 = df2[df2['data_type'] == 'Slopes']
Slopes_main = df3['data']




GD_main = []
for ii in geoDs_main:
    ii = eval(ii)
    GD_main.extend(ii)
S_main = []
for ii in Slopes_main:
    ii = eval(ii)
    S_main.extend(ii)
    
xran = np.arange(min(GD_main), max(GD_main), grain_p).tolist()
binned = np.digitize(GD_main, xran).tolist()
bins = [list([]) for _ in range(len(xran))]

for ii, val in enumerate(binned):
    bins[val-1].append(S_main[ii])

pct5 = []
pct95 = []
xran2 = []

for iii, _bin in enumerate(bins):
    if len(_bin) > 0:
        clim = clim_p
        pct5.append(np.percentile(_bin, 100 - clim))
        pct95.append(np.percentile(_bin, clim))
        xran2.append(xran[iii])

plt.fill_between(xran2, pct5, pct95, facecolor=clr, alpha=alpha_p, lw=lw_p)
#print max(xran2)      

plt.axvline(vlin_p, -1, 1.05, color='k', ls='--') 
plt.tick_params(axis='both', labelsize=fs-6)
plt.ylabel('Slope of DDR', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.xlim(-100, xlimit)


'''
plt.text(-6800, -0.2, "Geographic origins\n \n ", rotation=90, fontsize=fs+3)
plt.text(-6800, -1.1, "Geographic origins\nDifferential growth\n ", rotation=90, fontsize=fs+3)
plt.text(-6800, -2.0,  "Geographic origins\nDifferential growth\nDifferential agg",
         rotation=90, fontsize=fs+3)

plt.text(-100, 0.13, "Uniformly distributed\ngeographic ranges", fontsize=fs+4)
plt.text(14000, 0.13, "Latitudinal diversity\ngradient", fontsize=fs+4)
'''


fig.add_subplot(3,3,2)

typeof = 'spatial-null1'
ldg = 1

df2 = df[df['latDivGrad'] == ldg]
df2 = df2[df2['model_type'] == typeof]

df3 = df2[df2['data_type'] == 'geoDs']
geoDs_main = df3['data']
df3 = df2[df2['data_type'] == 'maxDs']
maxDs_main = df3['data']
df3 = df2[df2['data_type'] == 'Slopes']
Slopes_main = df3['data']


GD_main = []
for ii in geoDs_main:
    ii = eval(ii)
    GD_main.extend(ii)
S_main = []
for ii in Slopes_main:
    ii = eval(ii)
    S_main.extend(ii)
    
xran = np.arange(min(GD_main), max(GD_main), grain_p).tolist()
binned = np.digitize(GD_main, xran).tolist()
bins = [list([]) for _ in range(len(xran))]

for ii, val in enumerate(binned):
    bins[val-1].append(S_main[ii])

pct5 = []
pct95 = []
xran2 = []

for iii, _bin in enumerate(bins):
    if len(_bin) > 0:
        clim = clim_p
        pct5.append(np.percentile(_bin, 100 - clim))
        pct95.append(np.percentile(_bin, clim))
        xran2.append(xran[iii])

plt.fill_between(xran2, pct5, pct95, facecolor=clr, alpha=alpha_p, lw=lw_p)
    
plt.axvline(vlin_p, -1, 1.05, color='k', ls='--') 
plt.tick_params(axis='both', labelsize=fs-6)
plt.ylabel('Slope of DDR', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.xlim(-100, xlimit)




fig.add_subplot(3,3,4)

typeof = 'spatial-null2'
ldg = 0
clr = 'r'

df2 = df[df['latDivGrad'] == ldg]
df2 = df2[df2['model_type'] == typeof]

df3 = df2[df2['data_type'] == 'geoDs']
geoDs_main = df3['data']
df3 = df2[df2['data_type'] == 'maxDs']
maxDs_main = df3['data']
df3 = df2[df2['data_type'] == 'Slopes']
Slopes_main = df3['data']


GD_main = []
for ii in geoDs_main:
    ii = eval(ii)
    GD_main.extend(ii)
S_main = []
for ii in Slopes_main:
    ii = eval(ii)
    S_main.extend(ii)
    
xran = np.arange(min(GD_main), max(GD_main), grain_p).tolist()
binned = np.digitize(GD_main, xran).tolist()
bins = [list([]) for _ in range(len(xran))]

for ii, val in enumerate(binned):
    bins[val-1].append(S_main[ii])

pct5 = []
pct95 = []
xran2 = []

for iii, _bin in enumerate(bins):
    if len(_bin) > 0:
        clim = clim_p
        pct5.append(np.percentile(_bin, 100 - clim))
        pct95.append(np.percentile(_bin, clim))
        xran2.append(xran[iii])

plt.fill_between(xran2, pct5, pct95, facecolor=clr, alpha=alpha_p, lw=lw_p)
        
plt.axvline(vlin_p, -1, 1.05, color='k', ls='--') 
plt.tick_params(axis='both', labelsize=fs-6)
plt.ylabel('Slope of DDR', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.xlim(-100, xlimit)

#plt.text(-4500, 0.0, "Geographic origin/Env-niche model", rotation=90, fontsize=fs+4)


    
    
fig.add_subplot(3,3,5)

typeof = 'spatial-null2'
ldg = 1

df2 = df[df['latDivGrad'] == ldg]
df2 = df2[df2['model_type'] == typeof]

df3 = df2[df2['data_type'] == 'geoDs']
geoDs_main = df3['data']
df3 = df2[df2['data_type'] == 'maxDs']
maxDs_main = df3['data']
df3 = df2[df2['data_type'] == 'Slopes']
Slopes_main = df3['data']


GD_main = []
for ii in geoDs_main:
    ii = eval(ii)
    GD_main.extend(ii)
S_main = []
for ii in Slopes_main:
    ii = eval(ii)
    S_main.extend(ii)
    
xran = np.arange(min(GD_main), max(GD_main), grain_p).tolist()
binned = np.digitize(GD_main, xran).tolist()
bins = [list([]) for _ in range(len(xran))]

for ii, val in enumerate(binned):
    bins[val-1].append(S_main[ii])

pct5 = []
pct95 = []
xran2 = []

for iii, _bin in enumerate(bins):
    if len(_bin) > 0:
        clim = clim_p
        pct5.append(np.percentile(_bin, 100 - clim))
        pct95.append(np.percentile(_bin, clim))
        xran2.append(xran[iii])

plt.fill_between(xran2, pct5, pct95, facecolor=clr, alpha=alpha_p, lw=lw_p)
    
plt.axvline(vlin_p, -1, 1.05, color='k', ls='--') 
plt.tick_params(axis='both', labelsize=fs-6)
plt.ylabel('Slope of DDR', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.xlim(-100, xlimit)





fig.add_subplot(3,3,7)

typeof = 'spatial-null3'
ldg = 0
clr = 'b'

df2 = df[df['latDivGrad'] == ldg]
df2 = df2[df2['model_type'] == typeof]

df3 = df2[df2['data_type'] == 'geoDs']
geoDs_main = df3['data']
df3 = df2[df2['data_type'] == 'maxDs']
maxDs_main = df3['data']
df3 = df2[df2['data_type'] == 'Slopes']
Slopes_main = df3['data']


GD_main = []
for ii in geoDs_main:
    ii = eval(ii)
    GD_main.extend(ii)
S_main = []
for ii in Slopes_main:
    ii = eval(ii)
    S_main.extend(ii)
    
xran = np.arange(min(GD_main), max(GD_main), grain_p).tolist()
binned = np.digitize(GD_main, xran).tolist()
bins = [list([]) for _ in range(len(xran))]

for ii, val in enumerate(binned):
    bins[val-1].append(S_main[ii])

pct5 = []
pct95 = []
xran2 = []

for iii, _bin in enumerate(bins):
    if len(_bin) > 0:
        clim = clim_p
        pct5.append(np.percentile(_bin, 100 - clim))
        pct95.append(np.percentile(_bin, clim))
        xran2.append(xran[iii])

plt.fill_between(xran2, pct5, pct95, facecolor=clr, alpha=alpha_p, lw=lw_p)
    
plt.axvline(vlin_p, -1, 1.05, color='k', ls='--') 
plt.tick_params(axis='both', labelsize=fs-6)
plt.ylabel('Slope of DDR', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.xlim(-100, xlimit)

#plt.text(-4500, -0.05, "Env-niche model", rotation=90, fontsize=fs+4)



fig.add_subplot(3,3,8)

typeof = 'spatial-null3'
ldg = 1

df2 = df[df['latDivGrad'] == ldg]
df2 = df2[df2['model_type'] == typeof]

df3 = df2[df2['data_type'] == 'geoDs']
geoDs_main = df3['data']
df3 = df2[df2['data_type'] == 'maxDs']
maxDs_main = df3['data']
df3 = df2[df2['data_type'] == 'Slopes']
Slopes_main = df3['data']


GD_main = []
for ii in geoDs_main:
    ii = eval(ii)
    GD_main.extend(ii)
S_main = []
for ii in Slopes_main:
    ii = eval(ii)
    S_main.extend(ii)
    
xran = np.arange(min(GD_main), max(GD_main), grain_p).tolist()
binned = np.digitize(GD_main, xran).tolist()
bins = [list([]) for _ in range(len(xran))]

for ii, val in enumerate(binned):
    bins[val-1].append(S_main[ii])

pct5 = []
pct95 = []
xran2 = []

for iii, _bin in enumerate(bins):
    if len(_bin) > 0:
        clim = clim_p
        pct5.append(np.percentile(_bin, 100 - clim))
        pct95.append(np.percentile(_bin, clim))
        xran2.append(xran[iii])

plt.fill_between(xran2, pct5, pct95, facecolor=clr, alpha=alpha_p, lw=lw_p)
    
plt.axvline(vlin_p, -1, 1.05, color='k', ls='--') 
plt.tick_params(axis='both', labelsize=fs-6)
plt.ylabel('Slope of DDR', fontsize=fs)
plt.xlabel(x_lab, fontsize=fs)
plt.xlim(-100, xlimit)



plt.subplots_adjust(wspace=0.35, hspace=0.3)
#plt.savefig(mydir+'/Modeling/figs/SpatialModels.png', dpi=200, bbox_inches = "tight")
plt.savefig(mydir+'/figures/Fig5a.png', dpi=400, bbox_inches = "tight")
plt.close()
