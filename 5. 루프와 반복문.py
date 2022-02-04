#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Repeated steps

n = 5
while n > 0:
    print(n)
    n -= 1
print('-----')
print('end')
print(n)


# In[ ]:


# An Infinite Loop
## Super Busy!
## iteration value에 값지정을 안하는 경우
n = 0 
while n > 0:
    print('inf')
    print('loop')
print('end') # INF LOPP


# In[5]:


# break
while True:
    line = input('> ')
    if line == 'done' : 
        break # done을 치면 break(더이상 반복구문으로 돌아가지 않음))
    print(line)
print('Done!')


# In[7]:


# continue
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print('done')
print('Done!')


# In[10]:


# for loop
## What is the largest number?
num_lst = [9, 41, 12, 3, 74, 15]
fst = min(num_lst)

for i in num_lst:
    if i > fst:
        fst = i
print(fst)


# In[20]:


# for loop
## Function) What is the largest number?
def largest(lst):
    fst = lst[0]
    for i in lst:
        if i > fst:
            fst = i
    return fst

lst = [9, 41, 12, 3, 74, 15]
largest(lst)


# In[12]:


# for loop
## Counting in a loop
def counting(lst):
    cnt = 0
    for i in lst:
        cnt += 1
    return cnt

lst = [9, 41, 12, 3, 74, 15]
counting(lst)


# In[13]:


# for loop
## Summing in a loop
def summing(lst):
    s = 0
    for i in lst:
        s += i
    return s

lst = [9, 41, 12, 3, 74, 15]
summing(lst)


# In[14]:


# for loop
## Finding the Average in a Loop
def average(lst):
    cnt, s = 0, 0
    for i in lst:
        cnt += 1
        s += i
    return s/cnt

lst = [9, 41, 12, 3, 74, 15]
average(lst)


# In[17]:


# for loop
# Filtering in a Loop
lst = [9, 41, 12, 3, 74, 15]
for v in lst:
    if v > 20:
        print('larger than 20:', v)


# In[19]:


# for loop
## How to find the smallest value
def smallest(lst):
    fst = lst[0]
    for i in lst:
        if i < fst:
            fst = i
    return fst

lst = [9, 41, 12, 3, 74, 15]
smallest(lst)


# In[ ]:


# for loop
## is / is not
## None type과 Bool type에서만 사용하고 overuse X


# <h3><b>Exercises</b></h3>
# <p>Exercise 1: Write a program which repeatedly reads numbers until the user enters 'done'. Once 'done' is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using <span style='background-color: salmon'>try</span> and <span style='background-color: salmon'>except</span> and print an error message and skip to the next number.</P>
# Enter a number: 4  <BR>
# Enter a number: 5  <BR>
# Enter a number: bad data <BR> 
# Invalid input  <BR>
# Enter a number: 7  <BR>
# Enter a number: done  <BR>
# 16 3 5.333333333333333  <BR>

# In[9]:


lst = []
while True:
    i = input('Enter a number: ')
    try:
        num = float(i)
        lst.append(num)
    except:
        if i == 'done':
            print(sum(lst),len(lst),sum(lst)/len(lst))
            break
        else:
            print('Invalid input')


# In[ ]:




