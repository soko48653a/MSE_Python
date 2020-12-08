#!/usr/bin/env python
# coding: utf-8

# In[1]:


#예제 110번 : 아래 코드의 출력 결과를 예상하라

#if True :
#    if False:
#        print("1")
#        print("2")
#    else:
#        print("3")
#else :
#    print("4")
#print("5")

#======================================

if True :                                # 만약에 '참' 이라면
    if False:                                # 만약에 '거짓' 이라면
        print("1")                            # '1'과 '2' 출력
        print("2")
    else:                                    # 거짓이 아니라면
        print("3")                           # '3' 출력
else :                                   # '참'도 '거짓'도 아니라면
    print("4")                           # '4'출력
print("5")                               # 참일 때 '5' 출력

                    # '참' 일 때 -> 거짓이 아니기 때문에 '3'출력, 참이기 떄문에 '5'출력해서 결국 '3'과 '5'를 출력하게 된다


# In[ ]:




