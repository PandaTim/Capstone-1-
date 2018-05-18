import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# generate some sample data
import scipy.misc
a = 0
beta = -0.01
H = io.imread('hazy3.png')
D = io.imread('clear3.png')
H_gray = io.imread('hazy.png', as_grey=True)
D_gray = io.imread('clear.png', as_grey=True)
# downscaling has a "smoothing" effect
# D = scipy.misc.imresize(D, 0.3, interp='cubic')
# create the x and y coordinate arrays (here we just use pixel indices)
xx, yy = np.mgrid[0:H.shape[0], 0:H.shape[1]]
dividend_r = -(np.log(H[:,:,0] - a) - np.log(D[:,:,0] - a))
dividend_g = -(np.log(H[:,:,1] - a) - np.log(D[:,:,1] - a))
dividend_b = -(np.log(H[:,:,2] - a) - np.log(D[:,:,2] - a))
dividend_gray = -(np.log(H_gray*255 - a) - np.log(D_gray*255 - a))
'''
# create the figure
fig = plt.figure()
ax = fig.gca(projection='3d')
print(dividend_r)
#ax.plot_surface(xx, yy, H[:,:,0],rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
ax.plot_surface(xx, yy, dividend_r / beta,rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)

# show it
plt.show()
print("R channel")
fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.plot_surface(xx, yy, H[:,:,1],rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
ax.plot_surface(xx, yy, dividend_g / beta,rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
plt.show()
print("G channel")
fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.plot_surface(xx, yy, H[:,:,2],rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
ax.plot_surface(xx, yy, dividend_b / beta,rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
plt.show()
print("B channel")
'''
fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.plot_surface(xx, yy, H[:,:,2],rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
ax.plot_surface(xx, yy, (dividend_gray) / (beta),rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
plt.show()
print("Grayscale")
fig = plt.figure()
ax = fig.gca(projection='3d')
#ax.plot_surface(xx, yy, H[:,:,2],rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
ax.plot_surface(xx, yy, (dividend_r + dividend_g + dividend_b) / (3*beta),rstride=1, cstride=1, cmap=plt.cm.coolwarm,linewidth=0)
plt.show()
print("Average")
print(((dividend_r + dividend_g + dividend_b) / (3*beta))[124][96])