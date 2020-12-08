#!/usr/bin/env python
# coding: utf-8

# In[1]:


#예제 230 번 : 아래 코드의 실행 결과를 예측하라.

#def my_print (a, b) :
#    print("왼쪽:", a)
#    print("오른쪽:", b)

#my_print(b=100, a=200)

#=============================

def my_print (a, b) :       #my_print(a,b) 함수를 아래와 같이 정의한다.
    print("왼쪽:", a)       #("왼쪽: a값") 으로 출력한다.
    print("오른쪽:", b)     #("오른쪽: b값") 으로 출력한다.

my_print(b=100, a=200)      #my_print(a,b) 에 대해서 함수를 실행한다. 여기서 a와 b는 위치를 구분하는데에 사용되므로 주의한다.

#"왼쪽: 200" // "오른쪽:100" 으로 출력된다.


# In[ ]:




