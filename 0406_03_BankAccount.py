# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 생성자, 초기화 메서드로 초기 값 세팅
    def __init__(self, id, name, balance):
        # 클래스 내부에 멤버 변수를 숨겨달라 __를 붙이면 된다(이름 변경을 요구)
        # 인스턴스 멤버 변수
        self.__id = id
        self.__name = name 
        self.__balance = balance
    # 입금 
    def deposit(self, amount):
        self.__balance += amount 
    # 출금
    def withdraw(self, amount):
        self.__balance -= amount
    # 객체의 문자열을 요구하면(ToString() )
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1) # __str__ == toString 불러라
# print(account1.balance) # 고객의 잔고를 볼 수 있게 됨ㅠㅠ
# account.balance = 150000000 ==> 잔고가 공개 됨?? 의도치 않게 
#print(account1.__balance) # 출력하면 안 나옴
#클래스 외부에서는 아래와 같이 접근 == 백도어(변경된 이름)
#print(account1._BankAccount__balance) # 가려놓고 잔고 보고싶으면 볼 수 있음

#자동 완성
#account1.__id(아이디 보고 싶은데 private 마냥 숨겨져서 안나옴)


