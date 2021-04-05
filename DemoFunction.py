# DemoFunction.py
# 함수를 정의
def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

def mul(a, b) :
    return a * b

def divide(a, b) :
    return a / b

# 호출
print( add(1, 2) )
print( sub(4, 2) )
print( mul(3, 4) )
print( divide(4, 2) )

# 가변형과 불변형(int, float, 복소수, 튜플, 문자열)
print("---가변형, 불변형---")
a = 1.2
print( id(a) )
a = 2.3
print( id(a) )

print("---가변형---") # 주소가 바뀌지 않는다
lst = ["white", "blue"]
print( id(lst) )
lst.append("red")
print( id(lst) )

print("---전역 변수, 지역 변수---")
x = 5
def func(a) :
    return a + x

def func2(a) :
    x = 1
    return a + x

# 호출
print( func(1) )
print( func2(1) )
