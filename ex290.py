#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 290 번 :다음 코드의 실행 결과를 예상해보세요.

#class 부모:
#  def __init__(self):
#    print("부모생성")

#class 자식(부모):
#  def __init__(self):
#    print("자식생성")
#    super().__init__()

#나 = 자식()

#==========================

class 부모:                   #클래스 '부모'를 정의
  def __init__(self):         # __init__(self) -> '나' 를 다음과 같이 정의
    print("부모생성")         #"부모생성"을 출력하게 한다.

class 자식(부모):            #클래스 '자식(부모)'를 정의
  def __init__(self):        #__init__(self) -> 에서
    print("자식생성")        #"자식생성"을 출력하고,
    super().__init__()       #super() 함수를 이용해서 __init()로 다시돌아간다. ()-> self

나 = 자식()           #__init__(self=나)// 자식(부모) -> super().__init()에 의해서
                      #class 자식(부모)가 먼저 실행되고그 안에 __init__(slef) 함수에 의해서 class 부모가 다음으로 실행된다.
    
#따라서 자식생성, 부모생성 순서대로 출력되게 된다.


# In[ ]:




