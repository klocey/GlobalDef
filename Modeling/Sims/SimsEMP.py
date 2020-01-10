from __future__ import division
import gdal
import matplotlib
from mpl_toolkits.basemap import Basemap, addcyclic
import matplotlib.pyplot as plt
import numpy as np
from os.path import expanduser
from math import radians, cos, sin, asin, sqrt
import sys
from scipy import spatial, stats
from biom import load_table
import pandas as pd


mydir = expanduser("~/GitHub/asm")
mydir2 = expanduser("~/GitHub/asm/scripts/scripts/data/")
path = mydir2 + 'emp_deblur_90bp.release1.biom'

df = pd.DataFrame.from_csv(mydir2 + 'emp_qiime_mapping_release1_20170912_LatLon.tsv', sep='\t')
df2 = pd.DataFrame()

dat = load_table(path) 
ids1 = dat.ids().tolist()


sads = []
lats = []
lons = []
ids = []

for i in ids1:
    try:
        sad = dat.data(i)
        sads.append(sad)
    except:
        continue
    
    try:
        lat = df.loc[i][0] 
        lats.append(lat)
    except:
        continue
    
    try:
        lon = df.loc[i][1]
        lons.append(lon)
    except:
        continue
    
    ids.append(i)



df2['id'] = ids
df2['sad'] = sads
df2['lats'] = lats
df2['lons'] = lons



def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km



def render_data(fpath):
    
    ds = gdal.Open('DATA/'+fpath)
    data = ds.ReadAsArray()
    
    dlon = np.linspace(180, -180, data.shape[1]-1)
    dlon = np.flip(dlon)
    dlat = np.linspace(m.urcrnrlat, -90, data.shape[0]-1)
    dlat, dlon = addcyclic(dlat, dlon)
    
    return data
    

 
######################### GET LAT-LONS FOR MAP ################################

lat_viewing_angle = [20.0, 20.0]
lon_viewing_angle = [-180, 180]
rotation_steps = 200
lat_vec = np.linspace(lat_viewing_angle[0],lat_viewing_angle[0],rotation_steps)
lon_vec = np.linspace(lon_viewing_angle[0],lon_viewing_angle[1],rotation_steps)



######################### SIMULATION PARAMETERS ###############################
    
Ds = []
maxDs = []
numSamp = []
Sors = [] 
EnvD = []
As = []
xs = []
Ss = []
clrs = []
AccS = []
Names = []
Slopes = []

iM = int()

while 1 > 0:
    iM = np.random.choice(range(len(lats)), size=1, replace=False)[0] 
    if lats[iM] < 33 and lats[iM] > 31:
        if lons[iM] > -118 and lons[iM] < -116:
            break
        
lonM = lons[iM]
latM = lats[iM]
sadM = sads[iM]
print iM, lonM, latM, '\n'
#sys.exit()



######################### RUN SIMULATIONS #################################
#Is = []
#for i in range(10):
Is = np.linspace(0, 20000, 190).tolist()
Is = Is + np.linspace(18000, 20100, 10).tolist()
switch = 'off'

ct_m = 0
for index, i in enumerate(Is):
    print i
    
    
    fig = plt.figure(figsize=(10,10))
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=1, rowspan=1)
        
    plt.style.use('dark_background')
    #plt.style.use('classic')
        
    #################### MAKE MAP #####################
    plt.cla()
    m = Basemap(projection='ortho', lat_0=lat_vec[index], lon_0=lon_vec[index])
    
    # coastlines, map boundary, fill continents/water, fill ocean, draw countries
    m.drawmapboundary(color='w')
    m.drawcoastlines(color='w', linewidth=0.5)
    m.drawparallels(np.arange(-90.,120.,30.), color='w', linewidth=0.3)
    m.drawmeridians(np.arange(0.,420.,60.), color='w', linewidth=0.3)
    
    x, y = m(lons, lats)
    plt.scatter(x, y, marker='o', c='lime', s=10, edgecolors='lime', 
        linewidths=0.2, alpha=0.7)
    
    ######################## MODEL COMMUNITIES #######################

    Ds2 = []    
    Sor2 = []
    EnvD2 = []
    Ds2 = []   
    s_by_s = []
          
    ct = 0
    while ct < 200:
            
        i1, i2 = np.random.choice(range(len(lats)), size=2, replace=False)
        
        lon1 = lons[i1]
        lat1 = lats[i1]
        sad1 = sads[i1]
        
        lon2 = lons[i2]
        lat2 = lats[i2]
        sad2 = sads[i2]
        
        d = haversine(lon1, lat1, lon2, lat2)
        if d > i or np.isnan(d) == True: 
            continue
            
        sadr = np.asarray([sad1, sad2])
        sadr = np.delete(sadr, np.where(~sadr.any(axis=0))[0], axis=1)
        sad3 = sadr[0]
        sad4 = sadr[1]
        
        pair = np.asarray([sad3, sad4])
        dis = 1 - spatial.distance.pdist(pair, metric='braycurtis')[0]#/len(sad3)
        if np.isnan(dis) == True or dis < 0 or dis > 1: 
            continue
        
        Sor2.append(dis)
        Ds2.append(d)
        #print np.round(i,2), ct

        ct += 1
        
      
    try: 
        Ds3 = np.array(Ds2)/max(Ds2)
    except:
        Ds3 = np.zeros(len(Ds2))
    
    try: 
        slope, intercept, r_value, p_value, std_err = stats.linregress(Ds3, Sor2)
    except:
        slope = 0.0
        
    if np.isnan(slope) == True or np.isinf(slope) == True:
        slope = 0.0
        
    Sor2 = np.array(Sor2)/max(Sor2)
    
    print ct_m, np.round(i, 2),
    print '|  BC:', np.round(np.mean(Sor2), 4),
    print ct_m, ' : slope:', np.round(slope,3), '\n'
       
    avgD = np.mean(Ds2)
    
    '''
    if avgD > 7000:
        cor_s = np.abs(7000 - avgD)
        cor_s = 1 - (600/(600+cor_s))
        dif = np.abs(slope - 0.0) 
        slope = slope + cor_s*dif
    '''
    
    Sors.append(np.mean(Sor2))
    Ds.append(avgD)
    Slopes.append(slope)
    maxDs.append(max(Ds2))
    
    
    fs = 14
    
    print ct_m, np.round(i, 2),
    print '|  BC:', np.round(np.mean(Sor2), 4),
    Ds3 = np.array(Ds2)/max(Ds2)
    Sor2 = np.array(Sor2)/max(Sor2)
        
    '''
    try:
        slope, intercept, r_value, p_value, std_err = stats.linregress(Ds3, Sor2)
    except:
        print 'fail:,'
        print slope, len(Sor2), len(Ds2)
        print min(Ds3), max(Ds3)
        print min(Sor2), max(Sor2)
        sys.exit()
    '''
            
    print ' : slope:', np.round(slope,3), '\n'
    
    avgD = np.mean(Ds2)
    Sors.append(np.mean(Sor2))
    Ds.append(avgD)
    Slopes.append(slope)
    
    
    
    
    ######### Plot 3
    ax4 = plt.subplot2grid((3, 3), (0, 1), colspan=2, rowspan=1)
    plt.scatter(Ds, Slopes, s=20, edgecolors='lime', facecolors='none', 
                    linewidths=1.25, alpha=1.0)
    
    if avgD >= 7000:
        switch = 'on'
    if switch == 'on':
        plt.axvline(7000, -1, 1.05, color='w', ls='--')

    plt.setp(ax4.get_xticklabels(), rotation=30, horizontalalignment='right')
    plt.tick_params(axis='both', labelsize=fs-5)
    plt.ylabel('Slope of DDR', fontsize=fs-2)
    plt.xlabel('Average distance between sample locations', fontsize=fs-1)
    #plt.xlim(-300, 10500)

    plt.subplots_adjust(wspace=0.55, hspace=0.05)
    plt.savefig(mydir+'/figures/emp/Fig'+str(ct_m)+'-'+str(np.round(i,2))+'.png', 
            dpi=400, bbox_inches = "tight")
    plt.close()
    ct_m += 1
    
    