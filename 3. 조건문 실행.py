#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Conditional Steps
x = 5
if x < 10:
    print('smaller')
else:
    print('bigger')


# In[3]:


# Nested Decisions
x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All Done')


# In[4]:


# Two-way Decisions
x = 4

if x > 2:
    print('Bigger')
else:
    print('Not bigger')
    
print('All Done')


# In[9]:


# Multi-way
## if-elif-elseb
x = int(input())

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
    
print('All Done')


# In[12]:


# try-except
## X overuse
a = 'ny'
try:
    int_a = int(a)
except:
    print('error')
    print('str', a)


# In[15]:


# try-except 2
astr = 'Bob'
try:
    print('Hello')
    # 여기서 오류가 생기므로 여기부터 except로 넘어감
    ## 따라서 여기에 try-except를 쓰는 게 맞음
    istr = int(astr) 
    print('There')
except:
    istr = -1

print('Done',istr)


# In[16]:


# Sample try-except
rawstr = input('num: ')
try:
    ival = int(rawstr)
except:
    ival = -1
    
if ival > 0:
    print('good')
else: # elif ival == -1:
    print('not a num')


# In[ ]:





# ## Exercise
# ### 초과근무 급여 계산
# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours. <br>
# Enter Hours: 45  
# Enter Rate: 10  
# Pay: 475.0  

# In[21]:


hr = float(input('Enter Working hours: '))
rate = float(input('Enter Rate: '))
if hr > 40:
    hr_exceed = hr - 40
    pay = 40*rate + hr_exceed*1.5*rate
else:
    pay = hr*rate

print(pay)


# ### 초과근무 급여 계산 - try-except 활용 
# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:  
# <hr>
# Enter Hours: 20 <br>
# Enter Rate: nine  <br>
# Error, please enter numeric input  <BR>
# <hr>
# Enter Hours: forty  <br>
# Error, please enter numeric input
# 

# In[26]:


try:
    hr = float(input('Enter Working hours: '))
    rate = float(input('Enter Rate: '))
    if hr > 40:
        hr_exceed = hr - 40
        pay = 40*rate + hr_exceed*1.5*rate
    else:
        pay = hr*rate

    print(pay)
except:
    print('Error, please enter numeric input')
    quit()


# In[1]:


# 모범답안
try:
    hr = float(input('Enter Working hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    quit()
    
if hr > 40:
    hr_exceed = hr - 40
    pay = 40*rate + hr_exceed*1.5*rate
else:
    pay = hr*rate

print(pay)


# In[ ]:




