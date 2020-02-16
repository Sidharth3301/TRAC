import numpy as np

import matplotlib.pyplot as pltfrom scipy.fftpack import fft
from math import pi


x=np.loadtxt(r'C:\Users\Sidharth S Nair\Downloads\vela_Pulsar.mbr',usecols=(0))
y=np.loadtxt(r'C:\Users\Sidharth S Nair\Downloads\vela_Pulsar.mbr',usecols=(1))
max1=max(x)
min1=min(x)
max2=max(y)
min2=min(y)
x1=np.reshape(x,(512,-1),order='F')
fs=1/(33000000)
x2=fft(x1)
for k in x:
  
