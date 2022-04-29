#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''(1 . you have to write a fun which will take string and return a len of 
it without using a inbuilt fun len)'''


# In[23]:


def que1(s):
    l=[]
    if type (s)==str:
        for i,j in enumerate (s):
            l.append(i)
        return max(l)    


# In[24]:


s="HI HOW ARE YOU"


# In[25]:


que1(s)


# In[26]:


'''2. write a fun which will be able to print an index of all premitive element which you will pass '''


# In[30]:


def que2(a):
    if type(a)==int or type(a)==str or type(a)==tuple or type(a)==list  or type(a)==set:
        for i,j in enumerate (a):
            print("index = ",i, 'of ',j)


# In[34]:


que2([3,45,89,75])


# In[35]:


'''3 . Write a fun which will take input as a dict and give me out as a list of all the values 
even in case of 2 level nesting it should work '''


# In[31]:


def que3(c):
    l=[]
    if type(c)==dict:
        for i in c:
            if type(c[i])== int :
                l.append(c[i])
            elif type (c[i])==complex or type(c[i])==set:
                s=str(c[i])
            elif type(c[i])== str:
                continue
            elif type(c[i])== dict:
                l.extend(list(c[i].values()))
            else:
                l.extend(list(c[i]))
    print(l) 


# In[32]:


a={ 'INDIA':966,'b':[45,85,91,34,28,61],'c':(45,'hi','jk',65),'all':{
    'a':4586 ,'f':'hello'
}
}


# In[33]:


que3(a)


# In[36]:


'''4  .write a fun which will take another function as an input and return me an output '''


# In[59]:


def que4(len(d)):
    if d ==str:
        print(len)


# In[61]:


'''write a function whihc will take multiple list as a input and give me concatnation of all the element as 
and output'''


# In[79]:


def que5(a,b,c,d):
    l=[]
    if type(a)==list or type(b)==list or type(c) == list or type(d) == list:
        for i in (a,b,c,d):
            l.extend(i)
    return(l)        


# In[80]:


que5(a,c,b,d)


# In[85]:


a,b,c,d = [45,45,36,28,90,91,36,91,250],[64,92,31,75],[71,29,86],[20.35,60,28]


# In[81]:


'''write a function which will be able to take a list as an input return an index of each element 
like a inbuilt index function but even if we have repetative element it should return index '''


# In[94]:


def que5(g):
    if type(g)==list:
        for i,j in enumerate (g):
            print ("index is",i,"of",j)       


# In[95]:


que5(a)


# In[ ]:




