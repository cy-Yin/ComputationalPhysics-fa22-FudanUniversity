# python 3.8.13
# sunspots_FFT.py

# Created on Nov 5 12:04:02 2022
# version: 1.0
# @author: yinchaoyang
# --- utf-8 ---

# calculate the Fourier transform of the sunspot data 
# and then make a graph of the magnitude squared |c_k|^2 
# of the Fourier coefficients as a function of k.

import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
import os

time = []
data = []
# Load the sunspots.txt
basePath = os.path.abspath(__file__)
parentDirectory = os.path.dirname(basePath)
with open(os.path.join(parentDirectory, "sunspots.txt"), 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        tm, dt = line.split('\t')
        time.append(int(tm))
        data.append(float(dt))

# fast fourier transform
N = len(data)
fs = N      # sampling frequency
ts = 1 / fs # sampling period
freq = np.arange(0, 1, ts) * fs # 1 / N month^-1 as the unit
data_fft = fft(data, N)[1:int(freq[-1] / 2)]

plt.plot(time, data)
plt.show()

# Plot the the magnitude squared |c_k|^2 
# of the Fourier coefficients as a function of k.
plt.plot(freq[1:int(freq[-1] / 2)], np.abs(data_fft / N)**2)
print("k = 24 / %d month^-1" % N)
plt.xlabel('Freq $\qquad (1/%d \quad month^{-1}$)' % N)
plt.ylabel('FFT Amplitude')
plt.ylim(0, 250)
plt.show()
