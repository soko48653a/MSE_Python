#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 180 번 : 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.

low_prices  = [100, 200, 400, 800, 1000]      #리스트 두 개 정의
high_prices = [150, 300, 430, 880, 1000]

volatility = []              #

for A in range(len(low_prices)) :          #for A in B 문 사용 // len(low_prices) -> low_prices 리스트의 길이 만큼 range 특정 (5)
    volatility.append(high_prices[A] - low_prices[A])      #append(high_prices[A]- low_prices[A]) -> 고가와 저가의 차 = 변동폭을 append 함수를 이용하여
                                                           #volatility 에 추가한다.
                                                           #append() 함수는 리스트에 요소를 추가하는데에 사용된다.
print(volatility)    #volatility 를 출력  (150-100, 300-200, 430-400, 880-800, 1000-1000)


# In[ ]:




