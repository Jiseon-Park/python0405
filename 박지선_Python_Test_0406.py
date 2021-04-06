# 박지선_Python_Test_0406.py

#1
class BankAccount:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)

print("--" * 30)

#2
# 출력 결과 : 
# Id : 1, 이름 : 전우치, 월급 : 2000000원 입니다.

class Developer :


    def __init__(self, id, name) :
        self.id = id
        self.name = name
    def getSalary(self, day) : 
        self.day = day 
        salary = self.day * 100000    
        print(salary)
    def __str__(self) :
        return "Id : {0}, 이름 : {1}, 월급 : {2}원 입니다.".format(
            self.id, self.name, self.day * 100000
        )

a = Developer(1, "전우치")
a.getSalary(20)
print(a)

# 3
"""
하루 일당 10만원 10일 일한 사람의 출력 결과
Id : 2, 이름 : 김, 월급 : 1000000원 입니다.
4000000

하루 일당 20만원 20일 일한 사람의 출력 결과
Id : 3, 이름 : 이, 월급 : 4000000원 입니다.
"""
class WebDeveloper(Developer) :
    def __init__(self, id, name) :
        Developer.__init__(self, id, name) 
    def getSalary(self, day) : 
        self.day = day 
        salary = self.day * 200000    
        print(salary)
    def __str__(self) :
        return "Id : {0}, 이름 : {1}, 월급 : {2}원 입니다.".format(
            self.id, self.name, self.day * 200000 
        )

b = Developer(2, "김")
b.getSalary(10)
print(b)

c = WebDeveloper(3, "이")
c.getSalary(20)
print(c)

# 4.
"""
모듈은 하나의 파일에 다수의 함수나 클래스를 정의하는 것을 뜻한다.
패키지는 폴더 안에 다수의 모듈을 저장해서 관리하는 것을 뜻한다.
함수는 반복해서 사용하기 위한 코드의 묶음으로 미리 정의 한 후 사용할 때 
호출하는 것을 뜻한다.
클래스는 객체를 생성하기 위해 변수와 메서드를 정의하는 일종의 틀을 뜻한다
"""

# 5.
"""
import re를 불러와
re.search() 함수를 사용하여 원하는 값을 불러올 수 있다
"""
import re

# 내가 푼 방법
print("--" * 20)
info = {"이름" : "지", "번호" : "1", "우편번호" : "12345"}

for k in info.keys() :
    if re.search("우편번호", k) :
        print("우편 번호 : {0}".format(info["우편번호"]))

# 정답
print(re.search("\d{5}", "우리 동네 우편 번호 53000"))
print(bool(re.search("\d{5}", "우리 동네 우편 번호 53000")))

# ++ 다른 예시 ++ 파이썬 아이들로 실행했을 때
# s = "Apple is a big company and apple is delicious"
# c = re.compile("apple")
# c.findall(s)
# c = re.compile("apple", re.I)
# c.findall(s)

# s = """
# Gee Gee Gee
# 너무 부끄러워
# 쳐다 볼 수 없어
# """
# c = re.compile("^.+")
# c.findall(s)

# c = re.compile("^.+", re.M)
# c.findall(s)




    



