#!/usr/bin/env python
# coding: utf-8

# In[18]:


#예제 270 번 : 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.


#종목명	종목코드	PER	PBR	배당수익률
#삼성전자	005930	15.79	1.33	2.83
#현대차	005380	8.70	0.35	4.27
#LG전자	066570	317.34	0.69	1.37

#=================================

class stock:                                                #stock 이라는 클래스를 설정한다. 클래스는 함수 묶음을 의미한다.
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend



종목 = []      #리스트 설정

삼성 = stock("삼성전자", '005930', 15.79, 1.33, 2.83)        #리스트에 3가지 값 저장
현대차 = stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)                #'종목'이라는 리스트에 삼성, 현대차, LG전자 요솟값을 각각 추가한다.
종목.append(현대차)
종목.append(LG전자)

for A in 종목:             #for A in B 문을 사용한다.
    print(A.code, A.per)    #code 클래스와 per 클래스를 바인딩할 수 있게 된다. 


# In[ ]:




