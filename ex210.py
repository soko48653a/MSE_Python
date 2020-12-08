#!/usr/bin/env python
# coding: utf-8

# In[3]:


#예제 210 번 : 아래 코드의 실행 결과를 예측하라.

#def message1():
#    print("A")

#def message2():
#    print("B")

#def message3():
#    for i in range (3) :
#        message2()
#        print("C")
#    message1()

#message3()

#===============================================

def message1():              #message1() 함수를 정의
    print("A")               #"A" 를 출력

def message2():             #message2() 함수를 정의
    print("B")              #"B" 를 출력

def message3():            #message3() 함수를  아래의 내용에 따라서 정의
    for A in range (3) :               #for A in B 구문을 사용, (0,1,2 범위에서)
        message2()                      #message2() 함수를 한 번 실행하고,
        print("C")                      #"C"를 출력한다.
    message1()                          #for 문에 의해서 위 조건문이 3번 반복하게 되고, 반복이 끝난 뒤 message1()함수를 실행한다.

message3()         #mmessage3()함수를 실행
                   #(B,C / B,C / B,C )/ A 로 출력된다.


# In[ ]:




