#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 120번 : 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값 (value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

#fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

#>> 좋아하는과일은? 한라봉
#오답입니다.

#=========================================

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}    #fruit 이라는 딕셔너리 생성

answer = input("좋아하는 과일은?")        # 변수 answer = input()함수 를 이용하여 생성
if answer in fruit.values():            # input() 함수에서 입력된 값 answer 가 fruit 딕셔너리의 값에 해당되면
    print("정답입니다.")                # "정답입니다"를 출력하고
else:                                  # 그렇지 않으면
    print("오답입니다.")                # "오답입니다"를 출력한다.


# In[ ]:




