from __future__ import division
import matplotlib.pyplot as plt
#import cartopy.crs as ccrs
import numpy as np
from os.path import expanduser
import sys
from scipy import spatial, stats

import cartopy.io.shapereader as shpreader
import shapely.geometry as sgeom
from shapely.ops import unary_union
from shapely.prepared import prep

from skimage import io

from math import pi
import random
import geopy
from geopy.distance import great_circle


mydir = expanduser("~/GitHub/GlobalDef")
sys.path.append(mydir+"/scripts")
import fxns


def get_abs(g_agg, gl_ab, e_opts1, e_land, Sg, lon, lat, DatLists, 
            map_lons, map_lats, s_o_lons, s_o_lats, typeof):

    
    # FIND GEOGRAPHIC MATCH    
    dist_from_o = []
    for si, val in enumerate(s_o_lons):
        d = fxns.haversine(val, s_o_lats[si], lon, lat)
        dist_from_o.append(d)
    
    dist_from_o = np.array(dist_from_o)    
    geo_match = (g_agg/(g_agg + dist_from_o))
    
    p_or_a_geo = np.random.binomial(1, geo_match, Sg) 

    lon = min(map_lons, key=lambda x:abs(x-lon))
    lat = min(map_lats, key=lambda x:abs(x-lat))
    
    i1 = map_lons.tolist().index(lon)
    i2 = map_lats.tolist().index(lat)
    
    # FIND ENVIRONMENTAL MATCH
    matches = []
    for ii, ls in enumerate(DatLists):
        e_val = ls[i2][i1]

        diff = np.abs(e_opts1[ii] - e_val)
        match = (0.1/(0.1 + diff)) 
        matches.append(match)
        
    avg_match = np.mean(matches, axis=0)

    p_or_a_env = np.random.binomial(1, avg_match, Sg)
    
    sad = []
    if typeof in ['model1', 'model2']:
        sad = geo_match * p_or_a_geo
    
    if typeof in ['model3', 'model4', 'model5', 'model6']: 
        sad = geo_match * p_or_a_geo * gl_ab
        
    if typeof in ['model7', 'model8']:
        sad = avg_match * p_or_a_env
        
    elif typeof in ['model9', 'model10']: 
        sad = avg_match * p_or_a_geo * gl_ab
        
    elif typeof in ['model11', 'model12']: 
        sad = avg_match * p_or_a_geo * gl_ab * e_land
    
    return sad




def randcolor():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())




def run_model(j, typeof, ldg):
    
    r = int(1000) # number of sites
    Sg = int(1000) # number of species
    num_iter = int(10000)
        
    lat = np.random.uniform(-90, 90) # starting latitude
    lon = np.random.uniform(-180, 180) # starting longitude
    loc1 = [lat, lon] # starting location
        
    DatLists = [PopDat, TopoDat, LandDat, VegDat, SeaDat, NppDat, 
                ChlDat, RainDat, IceDat, PermDat, SicsDat, LaiDat]
        
    geoDs = [] # geo distances 
    maxDs = [] # max geo distances
    Slopes = [] # DDR slopes
        
    
    s_o_lons = []
    s_o_lats = []
        
    if ldg == 0: 
        ed = float(pi*6371.0087714150598)
        method='great_circle'
        lons_lats = fxns.get_pts(Sg, loc1, ed, method)
        
        for lon_lat in lons_lats:
            s_o_lons.append(lon_lat[0])
            s_o_lats.append(lon_lat[1])
            
    elif ldg == 1:
        s_o_lats = np.random.normal(0, 25, Sg).tolist()
            
        for indx, val in enumerate(s_o_lats):
            if val < -90: 
                s_o_lats[indx] = -90
            elif val > 90: 
                s_o_lats[indx] = 90
            
        s_o_lons = np.linspace(-180, 180, Sg)
        
        
    terrestrial = np.random.binomial(1, 0.5, Sg) 
    # whether species is terrestrial or not
    # 1 == terrestrial
    # 0 == aquatic
    
    e_opts1 = [] # list to species environmental optimums
    for ie in range(12): # each species gets 12 env optimums
        opts = np.array(np.random.uniform(0, 1, Sg))
        e_opts1.append(opts)
              
    if typeof in ['model5', 'model6']:    
        g_agg = 10**np.random.uniform(1,3,Sg)
    else:
        g_agg = np.ones(Sg)*10**3
        
    gl_ab = 10**np.random.uniform(1,4,Sg)
    
    Ds = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 
          2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500,
          8000, 8500, 9000, 9500, 10000, 11000, 12000, 13000, 14000, 15000, 
          16000, 17000, 18000, 19000, 20015.1]
        
    ######################### RUN SIMULATIONS #################################
    for i in Ds:
        
        pts = []
        if i < 600:
            
            lat1, lon1 = loc1
            lat_o, lon_o = loc1
            ed = float(pi*6371)
            
            for ii in range(r):
                b = np.random.uniform(-180, 180)
                di = (np.random.uniform(i) + np.random.uniform(i))/2
            
                origin = geopy.Point(lat_o, lon_o)
                destination = great_circle(kilometers=di).destination(origin, b)
                lat1, lon1 = destination.latitude, destination.longitude
        
                pts.append([lon1, lat1])
            
        else: 
            method='great_circle'
            pts = fxns.get_pts(r, loc1, i, method) # get locations for samples
        
        geoDs2 = [] # mean geo distances 
        comDs2 = [] # community distances
        s_by_s = [] # site-by-species matrix
        
        for pt in pts:
            
            lon, lat = pt
            
            
            is_lnd = is_land(lon, lat)
            if is_lnd is False:
                terrestrial = 1 - terrestrial
            
            sad = get_abs(g_agg, gl_ab, e_opts1, terrestrial, Sg, lon, lat,
                    DatLists, map_lons, map_lats, s_o_lons, s_o_lats, typeof)
            
            if max(sad) != 0:
                s_by_s.append(sad)
            else: s_by_s.append([0]*Sg)
                
            
        s_by_s = np.asarray(s_by_s) # Site by species matrix

        #for ind1 in range(len(pts)):
        #    for ind2 in range(len(pts)):
        for ii in range(num_iter):
            ind1, ind2 = np.random.choice(range(len(pts)), 2, replace=False)
            if ind1 >= ind2: continue
                
            lon1, lat1 = pts[ind1]
            sad1 = s_by_s[ind1]
                    
            lon2, lat2 = pts[ind2]           
            sad2 = s_by_s[ind2]
                    
            if max(sad1) == 0 or max(sad2) == 0: continue
                    
            dx = fxns.haversine(lon1, lat1, lon2, lat2)
            
            sadr = np.asarray([sad1, sad2])
            sadr = np.delete(sadr, np.where(~sadr.any(axis=0))[0], axis=1)
            sad1 = sadr[0]
            sad2 = sadr[1]
            
            pair = np.asarray([sad1, sad2])
            dy = 1 - spatial.distance.pdist(pair, metric='braycurtis')[0]
                    
            if np.isnan(dy) == True or dy < 0 or dy > 1: continue
                    
            comDs2.append(dy)
            geoDs2.append(dx)
            
        g = np.array(geoDs2)/max(geoDs2)
        c = np.array(comDs2)/max(comDs2)
        slope, intercept, r_value, p_value, std_err = stats.linregress(g, c)
        
        avgD = np.mean(geoDs2)
        
        pstr = str(j)+' : '+str(np.round(i, 1))+' '+str(np.round(avgD,1))
        pstr += ' |  BC: '+str(np.round(np.mean(comDs2), 3))+' : slope:'
        pstr += str(np.round(slope,3))+' | model:'+str(typeof)
        print(pstr)
        
        geoDs.append(np.mean(geoDs2))
        Slopes.append(slope)      
        maxDs.append(max(geoDs2))
    
    geoDs, maxDs, Slopes = zip(*sorted(zip(geoDs, maxDs, Slopes)))
        
    clr = randcolor()
    return [list(geoDs), list(maxDs), list(Slopes), clr]



def is_land(x, y):
    return land.contains(sgeom.Point(x, y))




######################### GET LAT-LONS FOR MAP ################################
land_shp_fname = shpreader.natural_earth(resolution='50m',
                                       category='physical', name='land')

land_geom = unary_union(list(shpreader.Reader(land_shp_fname).geometries()))
land = prep(land_geom)


#m = plt.axes(projection=ccrs.PlateCarree())

img = io.imread('EnvData/SeaIceConcAndSnow.tif', as_gray=True)
data = plt.imread('EnvData/SeaIceConcAndSnow.tif')

map_lons = np.linspace(-180, 180, data.shape[1]-1)
map_lats = np.linspace(90, -90, data.shape[0]-1)

######################### LOAD ENV DATA ###########################################
TopoDat = io.imread('EnvData/Topography.tif', as_gray=True)
LandDat = io.imread('EnvData/LandSurfaceTemp.tif', as_gray=True)
VegDat = io.imread('EnvData/Vegetation.tif', as_gray=True)
SeaDat = io.imread('EnvData/SeaSurfaceTemp.tif', as_gray=True)
NppDat = io.imread('EnvData/Npp.tif', as_gray=True)
ChlDat = io.imread('EnvData/ChlorophyllConc.tif', as_gray=True)
RainDat = io.imread('EnvData/TotalRainfall.tif', as_gray=True)
IceDat = io.imread('EnvData/SeaIceConcAndSnow.tif', as_gray=True)
SicsDat = io.imread('EnvData/SeaIceConcAndSnow.tif', as_gray=True)
LaiDat = io.imread('EnvData/LeafAreaIndex.tif', as_gray=True)
PopDat = io.imread('EnvData/PopulationDensity.tif', as_gray=True)
PermDat = io.imread('EnvData/Permafrost.tif', as_gray=True)


OUT = open(mydir + '/Modeling/SimData/Data4Figs.txt', 'w+')
OUT.write('iteration\tdata_type\tmodel\tlatDivGrad\tdata\n')
OUT.close()


models = ['model1', 'model2', 'model3',
          'model4', 'model5', 'model6',
          'model7', 'model8', 'model9',
          'model10', 'model11', 'model12']



for iii in range(0, 10000):
    for typeof in models:
        ldg_mods = ['model2','model4', 'model6', 'model8', 'model10', 'model12']
        
        ldg = 0
        if typeof in ldg_mods: ldg = 1
        
        geoDs, maxDs, Slopes, clr = run_model(iii, typeof, ldg)
        
        OUT = open(mydir + '/Modeling/SimData/Data4Figs.txt', 'a+')
        OUT.write(str(iii)+'\tgeoDs\t'+typeof+'\t'+str(ldg)+'\t'+str(geoDs)+'\n')
        OUT.write(str(iii)+'\tmaxDs\t'+typeof+'\t'+str(ldg)+'\t'+str(maxDs)+'\n')
        OUT.write(str(iii)+'\tSlopes\t'+typeof+'\t'+str(ldg)+'\t'+str(Slopes)+'\n')
        OUT.write(str(iii)+'\tclrs\t'+typeof+'\t'+str(ldg)+'\t'+str(clr)+'\n')
        OUT.close()
