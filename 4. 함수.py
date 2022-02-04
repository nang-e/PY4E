#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# function
## def
## built-in


# <h3><strong>Exercise. 초과근무 급여 계산</strong></h3>
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called <span style='background-color:#fff5b1'>computepay</span> which takes two parameters (<span style='background-color:#fff5b1'>hours</span> and <span style='background-color:#fff5b1'>rate</span>) <br>
# Enter Hours: 45  
# Enter Rate: 10  
# Pay: 475.0  

# In[4]:


def computepay(hours,rate):
    if hours > 40:
        hr_exceed = hours - 40
        pay = 40*rate + hr_exceed*1.5*rate
    else:
        pay = hours*rate

    return pay


# In[5]:


computepay(45,10)

