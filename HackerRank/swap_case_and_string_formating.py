#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[29]:


x = 'HackerRank.com presents "Pythonist 2".'
c = ''
for i in x:
    if(i.islower()):
         c = c+chr(ord(i)-32)
    elif(i.isupper()):
        c = c+chr(ord(i)+32)
    else:
        c=c+i


# In[18]:








