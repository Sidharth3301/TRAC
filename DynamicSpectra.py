import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from math import pi

x=np.array(np.loadtxt('vela_Pulsar.mbr',usecols=(0)))
y=np.array(np.loadtxt('vela_Pulsar.mbr',usecols=(1)))
x1=np.reshape(x,(512,-1),order='F')
y1=np.reshape(x,(512,-1),order='F')
for i in range[0:939]:
    x2=np.reshape((np.mean(x[i:i+60],axis=0)),(512,-1),order='F')
    y2=np.reshape((np.mean(y[i:i+60],axis=0)),(512,-1),order='F')
    i+=60;
x3=fft(abs(x2))

fs=33e6
x4=np.linalg.matrix_power(x3,2)
t=np.arange(0,1,1/fs)
n=np.size(t)
fr=(fs/2)*np.linspace(0,1,n/2)
plt.subplot(2,1,1)
psd=plt.plot(fr,x4)
plt.subplot(2,1,2)
asd=plt.plot(fr,np.sqrt(x4))


    
