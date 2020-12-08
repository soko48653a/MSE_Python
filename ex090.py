#!/usr/bin/env python
# coding: utf-8

# In[1]:


#예제 90번 : 다음 코드에서 에러가 발생한 원인을 설명하라.

#>> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#>> icecream['누가바']
#Traceback (most recent call last):
#  File "<pyshell#69>", line 1, in <module>
#    icecream['누가바']
#KeyError: '누가바'

# icecream 이라는 명칭의 딕셔너리 {}를 생성하였다.
# icecream 딕셔너리 안에서 '누가바'를 사용해서 인덱싱하였다. 인덱싱은 튜플이나 딕셔너리의 요솟값을 찾기 위해서 사용하는 방법이다.
# icecream 딕셔너리 안에는 '누가바'라는 원소가 없으므로 오류가 발생 -> KeyError : '누가바'


# In[ ]:




