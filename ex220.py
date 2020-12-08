#!/usr/bin/env python
# coding: utf-8

# In[3]:


#예제 220 번 : 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

#===========================

def print_max(a, b, c) :            #print_max(a,b,c) 함수를 아래와 같이 정의한다.
    max_val = 0                     #max_val 변수 값을 설정한다.
    if a > max_val :                # print_max(a,b,c)에서 a가 max_val 보다 클 경우에는
        max_val = a                 #max_val 변수 값에 a를 대입한다.
    if b > max_val :                #b 값이 max_val 보다 클 경우에는
        max_val = b                 #max_val 변수 값에 b를 대입한다.
    if c > max_val :                #c 값이 max_val 보다 클 경우에는
        max_val = c                 #max_val 변수 값에 c를 대입한다.
    print(max_val)            #max_val 변수 값을 출력한다.
    
max(3,15,200)   #실행 예시


# In[ ]:




