#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 170 번 : 1~10까지의 숫자를 모두 곱한 값을 출력하는 프로그램을 for 문을 사용하여 작성하라.

result = 1       #result 변수 초기값 설정

for i in range(1, 11) :       #for A in B 문 사용 // range(P,Q) -> (P-1)부터 (Q-1) 까지 범위를 나타낸다.
    result =result * i        #result 변수 값에 i를 곱한 뒤 result 변수 값에 새로 대입한다. (i가 1~10이 될 때까지 for문 반복)
print(result)         #for 문이 끝난 뒤 result 변수 값 출력 // result=1*2*3*4*5*6*7*8*9*10 이 출력된다.


# In[ ]:




