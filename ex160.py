#!/usr/bin/env python
# coding: utf-8

# In[1]:


#예제 160번 : 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

#리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

#intra.h
#intra.c
#define.h

#==========================================================

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for A in 리스트:             # 리스트 내에서 A 정의
  split = A.split(".")        # 리스트 A원소들을 "."(마침표)를 기준으로 분할한다.(스플릿)
  if (split[1] == "h") or (split[1] == "c"):     # 만약 split 한 첫 번쨰 문자가 h 이거나 c 라면
    print(A)                 # A를 출력한다. (반복)
    
#split[1] => 스플릿 후 첫 번째 문자에 대해서 /// 'or' 연사자를 활용해서 .h '나' .c인 파일을 화면에 출력할 수 있게 된다.


# In[ ]:




