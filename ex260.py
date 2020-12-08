#!/usr/bin/env python
# coding: utf-8

# In[8]:


#예제 260 번 : 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

#class OMG : 
#    def print() :
#        print("Oh my god")

#>>> >>> myStock = OMG()
#>>> myStock.print()
#TypeError Traceback (most recent call last)
#<ipython-input-233-c85c04535b22> in <module>()
#----> myStock.print()

#TypeError: print() takes 0 positional arguments but 1 was given

#=================================

class OMG :             #클래스 OMG에 대해서
    def print(mystock) :       #print()를 다음과 같이 정의한다.
        print("Oh my god")         #print("Oh my god")

mystock = OMG()         #myStock 은 OMG() 클래스이다.
OMG.print(mystock)    # print() 에서 0이 지정되었다. 하지만 위처럼 OMG.print(mystock) 으로 실행되면 print()의 가로 안의 공간에 mystock
                      #이 들어가게 되므로 0 대신 1이 주어졌다고 에러가 발생한 것이다.
    
# 정의된 함수 print() 과 print(mystock) 이 달라서 생긴 문제이므로 def print() 를 def print(mystock) 로 바꾸면 해결된다.


# In[ ]:




