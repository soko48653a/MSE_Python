#!/usr/bin/env python
# coding: utf-8

# In[2]:


#예제 280 번 : 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

import random                # 난수(random)을 불러온다.


class Account:               #Account(계좌)라는 클래스를 만든다.
    account_count = 0        #초기값 설정

    def __init__(self, name, balance):     #__init__ 라는 함수를 설정, (self, name, balance) 변수를 가진다.
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []

        self.name = name
        self.balance = balance
        self.bank = "KB국민은행"

        num1 = random.randint(0, 999)          #무작위 값의 범위를 설정 randint
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001 의 형식을 취하게 된다. 계좌번호를 설정
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)
        
    def deposit(self, amount):
        if amount >= 1:
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:                #이자를 설정한다.
                self.balance = (self.balance * 1.01)


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):               #로그(내역)을 만들도록 함수를 정의한다.
        for amount in self.deposit_log:
            print(amount)

#==========================================================


k = Account("Song", 1000)
k.deposit(100)           #입금(deposit)
k.deposit(200)
k.deposit(300)
k.deposit_history()        #내역 저장

k.withdraw(100)         #출금(withdraw)
k.withdraw(200)
k.withdraw_history()       #내역 저장 


# In[ ]:




