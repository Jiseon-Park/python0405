# DemoOS.py / 각각 임포트 이름, 기능 기억하기!!
from os.path import *

# print( dir(os.path) )

print( abspath("python.exe") ) # 파일 경로
print( basename("c:\\python38\\python.exe") ) # 파일 네임
print( exists("c:\\python38\\python.exe") ) # 파일 존재 여부
print( getsize("c:\\python38\\python.exe") ) # 파일 크기

# 운영체제에 있는 명령어를 실행(cmd --> cd \, cd work2)
from os import *
# c:\work2 --> c: --> c:\work2
print("현재 작업 폴더 : ", getcwd() )
chdir("..")
chdir("c:\\work2")
print("현재 폴더 : ", getcwd() )

# 외부에 실행 파일 수행 --> 실행하면 메모장이 켜짐
# system("notepad.exe")

# 파일, 폴더 리스트
import glob
print( glob.glob("*.py") )
print("=" * 20)
for item in glob.glob("*.*") :
    print(item)