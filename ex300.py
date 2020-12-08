#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 300 번 : 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.

#try:
#    실행 코드
#except:
#    예외가 발생했을 때 수행할 코드
#else:
#    예외가 발생하지 않았을 때 수행할 코드
#finally:
#    예외 발생 여부와 상관없이 항상 수행할 코드

#아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에 적당한 코드를 작성해봅시다. else와 finally는 적당한 문구를 print하시면 됩니다.

#per = ["10.31", "", "8.00"]

#for i in per:
#    print(float(per))

#=================================================

per = ["10.31", "", "8.00"]           #per 리스트를 정의

for A in per:          #for A in B 문을 사용한다. per 리스트 안에 있는 A에 대해서
    try:                     #다음을 실행한다.
        print(float(A))        #float은 실수 숫자열을 의미한다.
    except:                 #예외인 경우에는
        print(0)             #'0'을 출력한다.
    else:                   #그 이외에는
        print("clean data")  #"clean data"를 출력한다.
    finally:                #for 문 실행 끝에 다음을 실행한다.
        print("변환 완료")   #"변환 완료"를 출력한다.
        
#10.31 을 실수 형태로 출력하고, 값이 없는 경우에 0을 출력하고 그 이외 경우에는 clean data를 실행하고 실행 후 마지막으로 "변환 완료"를 출력한다.


# In[ ]:




