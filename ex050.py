#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 50번 : 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

data = "039490     "

Result = data.rstrip()       #rstirp() 문자열 함수 명령어는 문자열의 오른쪽 공백을 없애준다.
print(Result)               #"039490     "에서 오른쪽 공백을 제거한 "039490"이 출력되게 된다.

#Result2 = data.lstrip() 로 하게되면 문자열의 왼쪽 공백을 없애게 된다.
#print(Result2)    문자열의 왼쪽 공백은 이미 없으므로, 똑같이 출력되게 된다.


# In[ ]:




