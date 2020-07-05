#!/usr/bin/env python
# coding: utf-8

# In[67]:


# Image procession 
# matplotlib imshow creates an image from a 2 dimensional numpy aray. the image will have one square for each element of the array

import matplotlib.pyplot as plt
import numpy as np

n = 4

#create an nxn numpy array
a =  np.reshape(np.linspace(0,1,n**2, endpoint = True), (n,n))

#First I instantiate the container
plt.figure(figsize=(12,4.5))

#use imshow to plot the array
#plt.subplot(131) 1X3 first  1 row  3 plots - first position (I guess)
plt.subplot(131)
plt.imshow(a,                        #numpy array generating the image
           cmap = 'gray',            #color map used to specify colors
           interpolation='nearest'   #algorithm used to blend square colors; with neareast colors will not be blended
          )
plt.xticks(range(n))
plt.yticks(range(n))
plt.title('Gray color map, no blending', y=1.02, fontsize = 12)

#the same array as above, but with different color map
plt.subplot(132)
plt.imshow(a, cmap ='viridis', interpolation = 'nearest')
plt.yticks([])
plt.xticks(range(n))
plt.title('Viridis color map, no blending', y=1.02, fontsize=12)

#the same array as above, bu with blending 
plt.subplot(133)
plt.imshow(a, cmap = 'viridis', interpolation = 'bicubic')
plt.yticks([])
plt.xticks(range(n))
plt.title('Viridis color map, bicubic blending', y=1.02, fontsize = 12)

plt.show()

print(a)


# # imsave

# In[70]:


n2 = 500

# create a nxn numpy array 
a = np.random.random((n2,n2))

#save the image to a file 'test.pnp' using the 'jet' color map to specify colors
plt.imsave('test.png',a,cmap='inferno')


# In[74]:


#RGB

n = 20 
m = 4 
# three nxm numpy arrays with randomly selected RGA coordinates
r = np.random.random((n,m))
g = np.random.random((n,m))
b = np.random.random((n,m))

plt.figure(figsize=(15,4))
plt.axes(aspect = 'equal')
plt.ylim(-0.7,3.7)
plt.xlim(-0.7, 19.7)

for i, j in [(i,j) for i in range(n) for j in range (m)]:

    #plot a square with color given by RGB coordinates
    plt.plot(i,j, 's', color=(r[i,j], g[i,j], b[i,j]), markeredgecolor='w', ms=42)
    
ax = plt.gca()
ax.set_axis_bgcolor('k')
plt.yticks([])
plt.xticks([])

plt.show()


# In[85]:


#imshow and imsave with rgb colors

import matplotlib.pyplot as plt
import numpy as np

n = 4

#create a 3-dimensional numpy array with randomly selected RGB coordinates
a = np.random.random((n,n,3))


plt.figure(figsize=(11,3))

plt.subplot(141)
r = a.copy()
r[:,:,[1,2]] = 0    #set green and blue coordinates to 0; this will display reds only
plt.yticks(range(n))
plt.xticks(range(n))
plt.title('Red component')
plt.imshow(r, interpolation='nearest')

plt.subplot(142)
g = a.copy()
g[:,:,[0,2]] = 0
plt.yticks(range(n))
plt.xticks(range(n))
plt.title('Green component')
plt.imshow(g, interpolation ='nearest')

plt.subplot(143)
b = a.copy()
b[:,:,[0,1]] = 0
plt.yticks(range(n))
plt.xticks(range(n))
plt.title('Blue component')
plt.imshow(b, interpolation = 'nearest')

plt.subplot(144)
plt.xticks(range(n))
plt.yticks([])
plt.title('RGB Mixture')
plt.imshow(a, interpolation='nearest')
plt.show()


# In[86]:


#imread

img_array = plt.imread('tiger.jpg')


# In[87]:


print(img_array)


# In[103]:


tiger = img_array/255 
print(tiger)


# In[102]:


plt.figure(figsize=(10,10))
plt.imshow(tiger)
plt.show()


# In[97]:


plt.figure(figsize=(10,6))
for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)
    plt.axis('off') # hide coordinate axes 
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)
    
plt.show()


# In[98]:


plt.figure(figsize=(6,6))
plt.imshow(tiger[:300,100:400,:])
plt.axis('off')
plt.show()


# In[107]:


red_tiger = tiger.copy()

red_tiger[:,:,[0,1]]= 0
plt.figure(figsize=(10,10))
plt.imshow(red_tiger)
plt.axis('off')
plt.show()


# In[ ]:




