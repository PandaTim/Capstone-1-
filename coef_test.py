# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 02:03:52 2018

@author: Panda
"""

import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# generate some sample data
import scipy.misc
def frange(x, y, jump):
  while x < y:
    yield x
    x += jump
a = 0
beta = -0.01
H = io.imread('hazy.png')
D = io.imread('clear.png')
H_gray = io.imread('hazy.png', as_grey=True)
D_gray = io.imread('clear.png', as_grey=True)
a_value_info = []
# downscaling has a "smoothing" effect
# D = scipy.misc.imresize(D, 0.3, interp='cubic')
# create the x and y coordinate arrays (here we just use pixel indices)
xx, yy = np.mgrid[0:H.shape[0], 0:H.shape[1]]
for i in frange(0, 3, 0.1) :
    gray_dist = - np.log(H_gray*255 - i) - np.log(D_gray*255 - i)/beta
    red_dist = - np.log(H[:,:,0] - i) - np.log(D[:,:,0] - i)/beta
    blue_dist = - np.log(H[:,:,1] - i) - np.log(D[:,:,1] - i)/beta
    green_dist = - np.log(H[:,:,1] - i) - np.log(D[:,:,1] - i)/beta
    aver_dist = (red_dist + blue_dist + green_dist) / 3
    if np.amin(gray_dist) > 0 and np.amin(red_dist) > 0 and np.amin(green_dist) > 0 :
        a_value_info.append((i, np.amax(aver_dist), np.amin(aver_dist)))
    else :
        print("i = " + str(i) + ", " + "gray_dist : " + str(np.amin(gray_dist))+ ", ")
        '''
    print("i : " + str(i))
    print("Grayscale : ")
    print(gray_dist)
    print("Red : ")
    print(red_dist)
    print("Blue : ")
    print(blue_dist)
    print("Green : ")
    print(green_dist)
    '''
    '''
    print("Hazy in grayscale : " + str(log(H_gray*255 - i) - log(D_gray*255 -i)))
    print("Clear in grayscale : " + str((np.average(D_gray*255 - i))))
    print("Hazy red channel value : " + str((H[:,:,0] - i)))
    print("Clear red channel value : " + str((D[:,:,0] - i)))
    print("Hazy green channel value : " + str((H[:,:,1] - i)))
    print("Clear green channel value : " + str((D[:,:,1] - i)))
    print("Hazy blue channel value : " + str((H[:,:,2] - i)))
    print("Clear blue channel value : " + str((D[:,:,2] - i)))'''
a_value_info = sorted(a_value_info, key = lambda x:x[1] - x[2])
for i in range(0, len(a_value_info)):
    print(a_value_info[i])
    print("\n")