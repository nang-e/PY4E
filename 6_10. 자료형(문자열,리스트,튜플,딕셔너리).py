#!/usr/bin/env python
# coding: utf-8

# # 파이썬 기초문법 - 자료형

# Why Python?
# >배우기 쉬움<br>
# 많은 라이브러리와 모듈로 다양한 분야에서 활용 가능<br>
# => numpy, pybrain, sklearn등을 이용한 ML, statsmodels을 이용한 데이터 통계, pandas, matplotlib등을 이용한 데이터 시각화, flask, django등을 이용한 웹프로그래밍 등<br>
# 가장 간결한 코드라인수로 개발이 빠르다 !

# In[294]:


# nbextensions


# 자료형이란 프로그래밍을 할 때 쓰이는 숫자, 문자열 등의 자료 형태로 저장되는 모든 것<br>
# => 가장 기본적인 형태 : 숫자, 문자열, 리스트, 튜플, 딕셔너리 등

# ## 변수(Variable)
# =(assignment) 기호 사용하여 변수 생성  
# 변수 이름 = 변수에 저장할 값  
# 다른 프로그래밍 언어는 자료형을 직접 지정해야 하지만 파이썬은 그러지 않아도 돼서 다소 간편!

# In[212]:


a = [1,2,3]


# In[213]:


# a변수가 가리키는 메모리 주소 확인 
id(a)


# In[214]:


# 변수 복사하고 싶은 경우
b = a
print(id(a)==id(b)) # a와 b의 값이 같음

# a와 b의 메모리 주소가 같기에 a값이 변하면 b의 값도 변함
a.append(4) # [1,2,3,4]
print(a)
print(b)


# In[211]:


# a의 값이 변함에 따라 b의 값이 변하는 걸 원치 않는 경우?
## [:], copy 모듈, 내장함수 copy 이용

### 1 [:] 이용
a = [1, 2, 3]
b = a[:]
print('[:]', id(a) == id(b) )

### 2 copy 이용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print('copy', id(a) == id(b)) 

### 3 리스트 자체함수 copy
a = [1, 2, 3]
b = a.copy()
print('list.copy()', id(a) == id(b)) 


# ## 숫자형(Number)

# ### 정수형(Integer)

# In[215]:


# 양의 정수
a = '123'
b = 123
print(type(a))
print(type(b))

# # 음의 정수
# b = -1
# print(b)

# # 0
# c = 0
# print(c)


# ### Float

# In[2]:


a = 1.2
print(a)
a = -2.4
print(a)

# 제곱승을 표현하고 싶을 때는 E (혹은 e)사용
a = 4E10
print(a)
a = 4e-10
print(a)


# ### 2,8,16진수
# 파이썬에선 기본적으로 10진수로 숫자를 나타냄.  
# 다른 진수의 형태로 숫자를 표현할 경우 2진수의 경우 0b, 8진수의 경우 0o, 16진수의 경우 0x의 접두어를 붙여주어야 한다.  
#   
#   
# ~~잘 쓰진 않음~~

# In[3]:


# 내장함수를 통해 숫자를 각 진수형태의 문자열로 변환 가능
# bin(): 2진수, oct():. 8진수, hex(): 16진수 
print(bin(42))
print(oct(42))
print(hex(42))

print(oct(0b101010)) # 내장함수 안의 인자가 꼭 10진수가 아니어도 됨

# int(문자열,2/8/10/16)을 통해 숫자로 다시 변환 가능
print(int('0b101010',2))
print(int('0o52',8))
print(int('0x2a',16))


# ### 복소수(Complex Number)
# 파이썬에서는 허수 *i* 대신 *j* 를 사용한다

# In[4]:


a = 1+2j
print(a)

# 복소수.real : 실수부분
# 복소수.imag : 허수부분
print(a.real)
print(a.imag)

# 복소수.conjugate() : 켤레복소수 반환
# abs(복소수) : ,복소수 절대값 반환
print(a.conjugate())
print(abs(a))


# ### 숫자연산
# 사칙연산 ( +, -, *, /)  
# 몫 반환( // )  
# 나머지 반환 ( % )  
# 제곱 ( ** )

# In[5]:


# 덧셈,뺄셈,곱셈,나눗셈
a = 3 ; b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 몫-나머지 반환
print(a//b)
print(a%b)

# 제곱
print(a**b)


# ## 문자열(String)  
#   <br>
# 문자열 string은 문자, 단어들로 구성된 문자들의 집합<br> 
# '' 혹은 "" 등의 인용부호로 둘러싸인 것

# ### 문자열 생성하는 방법

# In[6]:


# 문자열 안에 ' 혹은 "를 넣고 싶다면 문자열을 감싸는 전체 따옴표는 반대로
food = "python's favorite food is pizza"
food


# In[217]:


food = 'python\'s favorite food is pizza'


# In[7]:


# 혹은 \ 백슬래시를 이용해서 문자열 안에 따옴표를 포함할 수 있음
food = 'python\'s favorite food is pizza'
food


# In[218]:


# 여러 줄의 문자열을 작성하고 싶다면 따옴표 3개 !
# \n은 줄바꿈 (이스케이프 코드)
mul_line = '''
Life is too short
You need Python
'''
mul_line


# In[219]:


print(mul_line)


# ### 이스케이프 코드

# In[ ]:


\n \t \' \" 


# ### 문자열 연산
# 파이썬은 문자열도 연산이 가능하다 !

# In[18]:


a = 'Hello'
b = 'Nang-ni'

print(a+b)
print('='*30)
print((b+' ')*3)


# In[19]:


print(a-b)


# In[20]:


print(a/b)
# 단, 덧셈과 곱셈만 가능 


# ### 인덱싱, 슬라이싱
# 인덱싱: 무언가를 가리키는 것  
# 슬라이싱: 무언가를 잘라내는 것  
# 
# ![image-2.png](attachment:image-2.png)  
# 
# 위 사진과 같이 문자열의 각 문자마다 번호를 매길 수 있다.  
# **1이 아니라 0부터 시작**  
# 

# In[22]:


# 인덱싱
a = 'Life is too short, You need Python'
#-0 존재하지않고! -1이 마지막
print(a[0],a[3],a[-1]) # a의 0번쨰, 3번쨰, -1번쨰(뒤에서부터) 문자


# In[220]:


# 슬라이싱  [:4] [7:] a[-6: ]
# a[0:4] <-- 0 <= i < 4
a = 'Life is too short, You need Python'
print(a[0:4]) #a[a:b]
print(a[0:3]) # a에서 3번째 문자 = e => a:b슬라이싱은 b를 포함하지 않음!


# In[221]:


len(a)
a[0:34]


# In[26]:


print(a[5:]) # 5번째부터 끝까지
print(a[:9]) # 처음부터 9번쨰 직전까지(8번째 문자까지)


# In[222]:


# **슬라이싱을 통한 삽입은 불가!**
a = "Pithon"   
print(a[1])
a[1] = 'y'
#print(a)


# In[32]:


print(a[:1]) #P
print(a[2:]) #thon
a[:1]+'y'+a[2:]


# ### 문자열 포매팅
# 
# ![image-2.png](attachment:image-2.png)

# In[224]:


# 숫자 대입
print("I need %d apples" % 5) # 정수
print("Battery percent %f" % 0.7254) # 실수 그대로
print("Battery percent %.2f %%" % 0.7254) # 실수 소수점 자리 지정


# In[176]:


# 문자 대입
"I need %s apples" % 'five'


# In[177]:


# 두가지 동시에 대입
name = 'Na Yeon'
age = 23
"My name is %s, I am %d years old" % (name, age)


# In[225]:


"My name is %s, I am %d years old" % (name)


# In[226]:


"My name is %s, I am years old" % (name, age)


# In[178]:


# 공백
print("%10s" % "hi")
print("%-10sjane." % "hi") 


# **format 함수**

# In[230]:


# format 함수 --> {0} 값 바로 대입, {변수명} 지정해서 대입
print("I eat {0} apples".format(3)) 
print("I eat {0} apples".format('five'))

number = 7
print("I eat {0} apples".format(number))

# 2개 이상의 값을 넣을 경우 인덱스 항목이 format함수의 입력값으로 순서에 맞게 바뀜
day = 'three'
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))
print("I ate {1} apples. so I was sick for {0} days.".format(number, day))
n = 3; m =7;k = 10
print("n = {0},m={2},k={1}".format(n,m,k))

# 이름으로 넣기
print('my name: {name} and age {num}'.format(name = '나연',num = 23))

# 인덱스와 이름을 혼용해서 넣기
print('my name: {0} and age {num}'.format('나연',num = 23))


# **f 문자열 포매팅**

# In[231]:


name = '나연'
age = 23

f'나의 이름은 {name}입니다. 나이는 {age}입니다.'


# In[234]:


f'내이름은 {name}'


# In[180]:


age = 23
f'나는 내년이면 {age + 1}살이 된다'


# In[236]:


d = {'name':'나연', 'age':23}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
# 따옴표 주의!


# In[183]:


a = [13,23,33]
f'내 나이는 {a[1]}살!'


# In[184]:


y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.4f}')


# ### 문자열 관련 함수

# In[155]:


# count(): 개수 세기
a = 'house'
print(a.count('o'))
b = 'pizza'
print(b.count('z'))


# In[239]:


# find(),index() : 위치 알려주기
## find - -1을 반환? => 없는 문자다!
a = 'python is the best choice'
print(a.find('b'), a.find('k')) 
print(a[14])

## index - ValueError => 없는 문자다!
a = 'life is too short'
print(a.index('t'), a.index('o')) # 각 문자가 첫번째로 나온 자리의 index
#print(a.index('a'))


# In[157]:


# join() : 문자열 삽입
# 문자열.함수()
print(','.join('abcd')) 
print(','.join(['a', 'b', 'c', 'd', 'e']))


# In[160]:


# 소문자 / 대문자
print('hi'.upper()) #대문자
print('HI'.lower()) #소문자 
print('Hello'.upper())


# In[243]:


# 중요! 공백 지우기 strip
a = '  hell   o  '
print(a.lstrip()) # 왼쪽 공백
print(a.rstrip()) # 오른쪽 공백
print(a.strip()) # 양쪽 공백


# In[244]:


# 문자열 바꾸기
print(a.replace(' ', '@')) # replace('기존', '바꿀 값') 
a.replace(' ','')


# In[245]:


# split(): 문자열 나누기 - default가 띄어쓰기!
a = 'Life is too short'
print(a.split())
b = 'a:b:c :d'
print(b.split(':')) 


# In[248]:


# 문제 ! helo
s = '    hㄷe,,l,,  o '
s.replace(' ', '').replace(',', '').replace('ㄷ', '')


# ## 리스트
# <br> 
# 리스트?  
# lst = [요소1,요소2,..]    

# In[36]:


a = [] # 빈리스트
b = [1,2,3]
c = ['nang','ni','haru']
d = [1,2,'nang',['ni','haru']]

print(a,b,c,d,sep = '\n')


# ### 리스트 인덱싱
# 문자열 인덱싱처럼 리스트도 인덱싱이 가능하다! <br> 
# **리스트도 0부터 시작**

# In[37]:


a = [1,2,3]
print(a,a[0],a[-1],sep='\n')


# In[39]:


a[0]+a[2] # 인덱싱을 활용한 덧셈


# In[252]:


a = ['1',2,'3']
type(a[0])


# In[253]:


a[0]+a[2]


# In[255]:


# 중첩된 리스트
a = [1, 2, 3, ['a', 'b', 'c']]
print(a)
print(a[-1])
print(a[-1][0]) # 중첩 리스트에 포함된 값을 인덱싱을 통해 불러내기


# In[261]:


# 삼중리스트 연습하기 ๑˃̶͈̀Ⱉ˂̶͈́๑!
a = [1, 2, ['a', 'b', ['Life', 'is']]]

# 여기서 Life를 뽑아내려면 어떻게 해야할까용 (◍•ᴗ•◍)
a[2][2][0]
# + 여기서 is의 s를 뽑아내려면 어떻게 해야할까용 (◍•ᴗ•◍)
a[2][2][1][1]


# ### 리스트 슬라이싱

# In[45]:


a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[:2])
print(a[3:5])
print(a[3:]) 


# In[49]:


# 중첩된 리스트
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][1:]) 


# ### 리스트 연산
# +를 이용해 리스트끼리 덧셈 가능  
# *를 이용해 반복도 가능

# In[47]:


a = [1, 2, 3]
b = [4, 5, 6]
a + b


# In[48]:


a*3


# In[51]:


# len(lst) : 리스트의 길이를 구하는 함수 => 튜플, 딕셔너리에도 활용 가능
a = [1, 2, 3]
len(a) 


# In[269]:


## 연산오류 주의 ##
a = [1, 2, 3]  
a = '2'
type(a) str(),int(), float()
#print(str(a[2]) + 'hi') # 값 뭐가 나올까요 ? ? 


# ### 리스트 수정 및 삭제

# In[57]:


a = [1, 2, 3]
a[2] = 4
print(a)


# In[58]:


# del 함수를 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1]
print(a)


# In[59]:


# del 객체
del a
print(a)


# ### 리스트 관련 함수

# In[60]:


# append(): 요소 추가
a = [1, 2, 3]
a.append(4)
a


# In[61]:


# sort() : 정렬
a = [1, 4, 2, 3]
a.sort()
a


# In[62]:


# 뒤집기
a = ['a', 'b', 'c']
a.reverse() 
a


# In[63]:


#인덱스 반환 lst.index(value,*start,*end)
a = [1, 2, 3]
a.index(3) # 값을 넣어야 함


# In[270]:


a = [1,2,3,7,2,4,3]
print(a.index(3))
print(a.index(3,3))


# In[73]:


# 여러개의 인덱스 찾고 싶다면...?
## filter 함수 사용
list(filter(lambda x:a[x]==3, range(len(a))))


# In[271]:


# 요소 삽입
a = [1, 2, 3]
a.insert(0, 4) # 값을 넣을 자리, 넣을 값
a


# In[79]:


# 요소 제거
a = [1, 2, 3, 4, 1, 2]
a.remove(2) # 같은 값이 여러번 들어가 있으면 제일 먼저 나온 값을 삭제
a


# In[81]:


# 리스트 안의 특정값 모두 제거하고 싶은 경우
print([i for i in a if i!=2])


# In[272]:


# 끄집어내기
a = [1, 2, 3]
a.pop() # 제일 마지막 값 꺼내서 삭제 a=[1,2]
a.pop(1) # 1번 인덱스의 값(a[1])을 꺼내서 삭제
a


# In[273]:


# 특정 요소 개수 세기
a = [1, 2, 3, 1]
a.count(1) # 1의 개수 세기


# In[274]:


# 리스트 확장
a = [1, 2, 3]
a.extend([4, 5]) # a += [4, 5]
print(a)
# a=[1,2,3]
# b=[4,5]
# print(a+b)
'''#
a = [1, 2, 3]
b = [4, 5]
a += b
#'''


# ## 튜플
# 
# 리스트와 비슷하지만 다른점이 존재함  
# 리스트는 [], 튜플은 ()  
# 리스트는 요소를 생성, 삭제, 수정이 가능하지만 튜플은 **불가능**하다!<br>
# ==> 따라서 프로그램 실행동안 값이 불변하길 원한다면 튜플 사용 (๑•͈ᴗ•͈)

# In[82]:


# 튜플 요소 삭제
t = (1,2,'a','b')
del t[0]


# In[83]:


# 튜플 요소 수정
t = (1,2,'a','b')
t[0] = 0


# In[ ]:


t1 = () 
t2 = (1,)       # 1개의 요소만 가지는 경우 반드시 , 붙여야 함.
t3 = (1, 2, 3)
t4 = 1, 2, 3    # 괄호 생략 가능
t5 = ('a','b',('ab','cd')) 


# In[278]:


t = (1,)


# In[279]:


type(t)


# ### 튜플 인덱싱 및 슬라이싱

# In[85]:


# 인덱싱
t1 = (1, 2, 'a', 'b')
t1[0]


# In[87]:


# 슬라이싱
t1 = (1, 2, 'a', 'b')
print(t1[1:3],t1[:2],t1[1:],sep='\n')


# ### 튜플 연산

# In[93]:


t1 = (1, 2, 'a', 'b')
t2 = (3,)


# In[94]:


t1+t2


# In[95]:


t2*3


# ### 튜플 길이 구하기

# In[96]:


t1 = (1, 2, 'a', 'b')
len(t1)


# ## 딕셔너리
# Key와 Value를 한 쌍으로 갖는 자료형  
# {key1:value1, key2:value2, ...}  
# 리스트나 튜플처럼 sequential하게 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻음  
# - Key는 고유한 값이기에 같은 이름으로 여러개 사용 불가  
# - Key값으로 리스트 사용 x, 튜플 사용 o -> 리스트는 값이 변할 수 있어서

# In[97]:


dic = {'name': 'nang', 'phone': '01011112222', 'birth': '1018'}
a = {1: 'hi'}
b = {'a': [1, 2, 3]}  # value에 리스트 넣을 수 있음


# ### 딕셔너리 쌍 추가, 삭제

# In[280]:


# 쌍 추가
a = {1: 'hi'}
a[2] = 'b'
print(a)

a['address']=['seoul','gangnam-gu']
print(a)


# In[282]:


# 쌍 삭제
print(a)
del a[1]
print(a)


# ### key를 이용해 value 얻기

# In[102]:


# 인덱싱이나 슬라이싱 대신 사용
grade = {'pey': 10, 'julliet': 99}
grade['pey'] 


# In[103]:


age = {'nang': 23, 'haru': 13, 'dal': 8}
age['dal']


# ### 딕셔너리 관련 함수

# In[113]:


# keys(): key 리스트 만들기
age = {'nang': 23, 'haru': 13, 'dal': 8}
print(age.keys())
print(list(age.keys()))


# In[116]:


for k in age.keys():
    print(k)


# In[114]:


# values() : value 리스트 만들기
age = {'nang': 23, 'haru': 13, 'dal': 8}
print(age.values())
print(list(age.values()))


# In[117]:


# items() : key, value 쌍 얻기 -> 튜플로 변환
age = {'nang': 23, 'haru': 13, 'dal': 8}
print(age.items())
print(list(age.items()))


# In[120]:


# clear() : key:value 쌍 지우기
print(age)
age.clear()
print(age)


# In[285]:


# get() : key로 value얻기
age = {'nang': 23, 'haru': 13, 'dal': 8}
print(age.get('nang')) # key가 nang일 때 value 얻기
print(age['nang'])


# In[123]:


print(age['nang'])
print(age.get('nang'))


# In[125]:


print(age['aqua'])


# In[126]:


print(age.get('aqua'))


# In[132]:


# 딕셔너리 안에 찾으려는 key값이 없을 경우 미리 정해 둔 default값을 가져오게 하고 싶은 경우
age.get('aqua','no')


# In[131]:


# 해당 key가 딕셔너리 안에 있는지 조사하기 (in)
age = {'nang': 23, 'haru': 13, 'dal': 8}
print('nang' in age)
print('charley' in age)


# ## 집합
# 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형  
# - 중복을 허용하지 않음 -> 중복 제거하기 위해 사용  
# - 순서가 없음 -> 인덱싱 지원 X, 인덱싱하려면 리스트나 튜플 등으로 변환 후 사용 가능

# In[134]:


s1 = set([1, 2, 3])
s2 = set('안뇽')
s3 = set()
print(s1, s2, s3)


# In[289]:


s = [1,1,1,1,1,2,2,2,3,3,4]
s = set(s)


# In[ ]:





# In[135]:


set('hello')


# In[137]:


# 인덱싱하고 싶은 경우 변환 후 사용
s1 = set([1, 2, 3])
lst = list(s1)
print(lst)
print(lst[0])
tpl = tuple(s1)
print(tpl)
print(tpl[0])


# In[291]:


s
s[0]


# ### 교집합,합집합,차집합 구하기

# In[ ]:


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 교집합 - '&' / intersection 함수
print('교집합')
print(s1 & s2)
print(s1.intersection(s2))
print(s2.intersection(s1))
# 합집합 - '|' / union 함수
print('합집합')
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))
# 차집합 - '-' / difference 함수
print('차집합')
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1)) 


# ### 집합 자료형 관련 함수들

# In[138]:


# 값 1개 추가하기 (add)
s1 = set([1,2,3])
s1.add(4)
print(s1)


# In[141]:


# 값 여러개 추가하기 (update)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)


# In[142]:


# 특정 값 제거하기 (remove)
s1.remove(4)
print(s1)


# ## 불
# 불 자료형이란 참 True 혹은 거짓 False로 나타내는 자료형 --> 이 두가지 값만 가질 수 있음

# In[143]:


a = True
print(type(a))
b = False
print(type(b)) 


# In[144]:


1 == 1


# In[145]:


2 < 1


# ### 참, 거짓
# ![image.png](attachment:image.png)

# ### 불 연산

# In[146]:


bool('python')


# In[147]:


bool('')


# In[148]:


bool(0)


# In[293]:


bool(3131)


# In[150]:


a = 13 ; b = 22
a is b # ==


# In[153]:


a is not b # !=


# In[ ]:





# In[4]:


# Exercise
ex = 'X-DSPM-Confidence: 0.8475'
ex = float(ex.split()[1])
type(ex)


# In[ ]:




