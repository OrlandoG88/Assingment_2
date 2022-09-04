#!/usr/bin/env python
# coding: utf-8

# In[1]:


even_numbers = [x for x in range(5) if x % 2 == 0]
squares      = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]


# In[2]:


even_numbers


# In[3]:


squares


# In[4]:


even_squares


# In[5]:


square_dict = {x: x * x for x in range(5)}
square_set  = {x * x for x in [1, -1]}


# In[6]:


square_set


# # Set comprehension is a bit challenging for me, I am not quite understanding how the out put is 1. Is it because oneis the unique square?
