#!/usr/bin/env python
# coding: utf-8

# In[1]:


#예제 130번 : 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다. 
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

import requests

btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']    #btc 딕셔너리에 저장되어 있는 값을 활용한다.

변동폭 = float(btc['max_price']) - float(btc['min_price'])       #변수 '변동폭'은 최고가와 최저가의 차이다.

시가 = float(btc['opening_price'])          #변수 '시가'는 최근 24시간 내 시작 거래금액을 의미한다.

최고가 = float(btc['max_price'])            #변수 '최고가'는 최근 24시간 내 최고 거래금액을 의미한다.

if (시가+변동폭) > 최고가:                 # (시가 + 변동폭)이 최고가보다 클 경우에는
    print("상승장")                        # "상승장"을 출력한다.
else:                                     # 그렇지 않으면
    print("하락장")                       # "하락장"을 출력한다.
    

# (변수 연산자 변수) > 변수 로 조건문을 나타내는 것도 가능하다.


# In[ ]:




