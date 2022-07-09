#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruitlist=['banana','mango','apple']


# In[2]:


fruitlist


# In[4]:


len(fruitlist)


# # Append

# In[5]:


fruitlist.append('grapes')


# In[6]:


fruitlist


# # Insert

# In[8]:


fruitlist.insert(2,'kiwi')


# In[9]:


fruitlist


# In[10]:


fruitlist.insert(3,'guava')


# In[11]:


fruitlist


# In[13]:


fruitlist.sort()


# In[14]:


fruitlist


# In[15]:


fruitlist.reverse()


# In[16]:


fruitlist


# In[17]:


fruitlist.insert(0,'papaya')


# In[18]:


fruitlist


# # Index

# In[20]:


fruitlist.index('grapes')


# In[21]:


fruitlist.index('apple')


# In[23]:


fruitlist.index('apple')


# In[24]:


fruitlist.index('kiwi')


# In[26]:


fruitlist[3]


# In[27]:


fruitlist[2]='pineapple'


# In[28]:


fruitlist


# In[30]:


fruitlist.sort()


# In[31]:


fruitlist


# In[32]:


fruitlist.reverse()


# In[33]:


fruitlist


# In[35]:


len(fruitlist)


# In[36]:


fruitlist[3]


# In[37]:


fruitlist[3]='jackfruit'


# In[38]:


fruitlist


# # Extend

# In[39]:


fruitlist.extend(['melon','avacado','orange'])


# In[40]:


fruitlist


# In[41]:


len(fruitlist)


# # Sort

# In[42]:


fruitlist.sort()


# In[43]:


fruitlist


# In[45]:


fruitlist


# # Reverse

# In[44]:


fruitlist.reverse()


# In[46]:


len(fruitlist)


# In[47]:


fruitlist.pop()


# In[48]:


fruitlist


# In[49]:


fruitlist.pop(2)


# In[50]:


fruitlist


# In[51]:


fruitlist.remove('mango')


# In[52]:


fruitlist


# In[56]:


fruitlist.clear()


# In[57]:


fruitlist


# # Length

# In[58]:


len(fruitlist)


# In[59]:


fruitlist.append('kiwi')


# In[60]:


fruitlist.append('apple')


# In[61]:


fruitlist


# In[63]:


fruitlist.clear()


# In[64]:


fruitlist


# In[65]:


del fruitlist


# In[67]:


numlist=[10,20,30,40,50,60]


# In[68]:


numlist


# In[71]:


numlist.extend([65,70,80])


# In[72]:


numlist


# In[77]:


len(numlist)


# In[84]:


numlist.index(60)



# In[85]:


numlist.pop(5)


# In[86]:


numlist


# In[89]:


numlist.append(4100)


# In[90]:


numlist


# In[91]:


numlist.remove(4100)


# In[92]:


numlist


# In[93]:


numlist[1]=14


# In[94]:


numlist


# In[95]:


len(numlist)


# In[96]:


numlist[5]=69


# In[97]:


numlist


# In[99]:


mobilelist=numlist


# In[100]:


mobilelist


# In[101]:


numlist


# # Tuples

# In[102]:


t1=(10,20,30,40,50)


# In[103]:


t1


# In[105]:


t1[0]


# In[106]:


t1[1]=866


# //tuples are immutable

# In[ ]:





# In[ ]:




