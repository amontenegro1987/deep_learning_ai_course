#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 

A = np.array([[56.0, 0.0, 4.4, 68.0],
              [1.2,104.0,52.0,8.0],
              [1.8,135.0,99.0,0.9]      
             ])

print(A)


# In[3]:


#Sum Vertically 1x4 matrix
#axis = 0 vertically axis = 1 horizontally
cal = A.sum(axis=0)
print(cal)


# In[4]:


percentage = 100*A/cal.reshape(1,4)
print(percentage)

#.reshape example of python broadcast (It is redundant because cal is already a 1,4 matrix)
#We've taken matrix A and devide it by a 1,4 matrix percentage


# In[ ]:




