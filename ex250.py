#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 250 번 : numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.

import numpy              #numpy 모듈을 사용한다.
for A in numpy.arange(0, 5, 0.1):           #for A in B 문을 사용 // arange(0, 5, 0.1) => 0부터 5까지 (5는 포함하지 않는다) 0.1 간격으로 실행
    print(A)               #A 출력


# In[ ]:




