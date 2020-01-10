from __future__ import division
import numpy as np
from math import radians, cos, sin, asin, sqrt, pi
import random
import geopy
#import sys
from geopy.distance import great_circle, geodesic
import shapely.geometry as sgeom

    
def antipodal(lat1, lon1):
    
    lat2, lon2 = float(), float()
    if lat1 == 0:
        lat2 == 0
    else:
        lat2 = lat1*-1
    if lon1 <= 0:
        lon2 = lon1 + 180
    else:
        lon2 = lon1 - 180
    return lat2, lon2
    

def is_land(x, y, land):
    return land.contains(sgeom.Point(x, y))
        
        
def get_pts(r, loc1, d, method, kind='global', land='none', ct=2):
    
    pts = []
    lat1, lon1 = loc1
    lat0, lon0 = loc1
    ed = float(pi*6371.0087714150598)
    
    while len(pts) < r:
        
        for i in range(ct):
        
            b = np.random.uniform(-180, 180)            
            di = float()
            
            if method == 'geodesic':
                lat2, lon2 = antipodal(lat1, lon1)
                ed = geodesic([lat1, lon1], [lat2, lon2]).kilometers
                di = np.random.uniform(ed)   
                origin = geopy.Point(lat1, lon1)
                destination = geodesic(kilometers=di).destination(origin, b)
                lat1, lon1 = destination.latitude, destination.longitude
            
            elif method == 'great_circle': 
                di = np.random.uniform(float(ed))
                #di = np.random.uniform(ed/2) + np.random.uniform(ed/2)
                origin = geopy.Point(lat1, lon1)
                destination = great_circle(kilometers=di).destination(origin, b)
                lat1, lon1 = destination.latitude, destination.longitude
            
        if kind == 'global':
            pts.append([lon1, lat1])
                
        elif kind == 'hemi':
            if method == 'geodesic':
                dist = geodesic([lat1, lon1], [lat0, lon0]).kilometers
                if dist < ed/2:
                    pts.append([lon1, lat1])
                    
            elif method == 'great_circle':
                dist = haversine(lon1, lat1, lon0, lat0)
                if dist < ed/2:
                    pts.append([lon1, lat1])
                
        elif kind == 'land':
            if is_land(lat1, lon1, land) == True:
                pts.append([lon1, lat1])
                    
        elif kind == 'water':
            if is_land(lat1, lon1, land) == False:
                pts.append([lon1, lat1])

    return pts




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
    km = 6371.0087714150598 * c
    return km



def randcolor():
    r = lambda: random.randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())

