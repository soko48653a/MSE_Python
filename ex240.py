#!/usr/bin/env python
# coding: utf-8

# In[1]:


#예제 240 번 : 아래 코드의 실행 결과를 예측하라.

#def 함수0(num) :
#    return num * 2

#def 함수1(num) :
#    return 함수0(num + 2)

#def 함수2(num) :
#    num = num + 10
#    return 함수1(num)

#c = 함수2(2)
#print(c)

#============================

def 함수0(num) :                #함수0(num) 함수를 정의한다.
    return num * 2             #num = num * 2 

def 함수1(num) :                #함수1(num) 함수를 정의한다.
    return 함수0(num + 2)      #함수0(num)에서 num 대신 (num+2) 를 대입한다.

def 함수2(num) :               #함수2(num) 함수를 아래와 같이 정의한다.
    num = num + 10             #num = num + 10  // num 값에 10을 더하고 대입한다.
    return 함수1(num)         #함수1(num) 에서 num 값을 대입한다.

c = 함수2(2)                 #c 는 함수2(2) 값이다.
print(c)                     #c 값을 출력

#num = 2 가 된다.
#num = 2 + 10 = 12 가 된다.
#함수1(num)에 num=12를 더한다.
#함수0(14)로 실행된다. 
#따라서 함수0(num) => num * 2 에 따라서 14 * 2 = 28이 출력되게 된다.


# In[ ]:




