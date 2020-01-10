from __future__ import division
import numpy as np
from os.path import expanduser
import pandas as pd

mydir = expanduser("~/GitHub/GlobalDef")
df = pd.read_csv(mydir + '/SimData/Moments.txt')
df = df[df['method'] == "'great_circle'"]    
df = df[df['sites'] == 1000]        
######################### FIGURE 2 ########################################

# Global Mean, Variance, Skewness
t = "'global'"
df2 = df[df['type'] == t]
mean = df2['mean'].tolist()
var = df2['var'].tolist()
skew = df2['skew'].tolist()

print(t, len(mean))
print('mean:',np.mean(mean),np.std(mean))
print('variance:',np.mean(var),np.std(var))
print('skewness:',np.mean(skew),np.std(skew))
print('\n')


# Hemispheric Mean, Variance, Skewness
t = "'hemi'"
df2 = df[df['type'] == t]
mean = df2['mean'].tolist()
var = df2['var'].tolist()
skew = df2['skew'].tolist()

print(t, len(mean))
print('mean:',np.mean(mean),np.std(mean))
print('variance:',np.mean(var),np.std(var))
print('skewness:',np.mean(skew),np.std(skew))
print('\n')


# Global Aquatic Mean, Variance, Skewness
t = "'water'"
df2 = df[df['type'] == t]
mean = df2['mean'].tolist()
var = df2['var'].tolist()
skew = df2['skew'].tolist()

print(t, len(mean))
print('mean:',np.mean(mean),np.std(mean))
print('variance:',np.mean(var),np.std(var))
print('skewness:',np.mean(skew),np.std(skew))
print('\n')


# Global Terrestrial Mean, Variance, Skewness
t = "'land'"
df2 = df[df['type'] == t]
mean = df2['mean'].tolist()
var = df2['var'].tolist()
skew = df2['skew'].tolist()

print(t, len(mean))
print('mean:',np.mean(mean),np.std(mean))
print('variance:',np.mean(var),np.std(var))
print('skewness:',np.mean(skew),np.std(skew))
print('\n')
