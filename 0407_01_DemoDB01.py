# 0407_01_DemoDB01.py
# SQLite를 사용하는 데모(로컬 데이터베이스)
import sqlite3

# 처음에는 데이터베이스 파일(또는 메모리)를 생성 ==> 연습용 그래서 파일에 저장 안함 
# ==> 끝나면 사라짐

con = sqlite3.connect(":memory:")

# SQL 구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()

# 저장소(테이블)을 만들기 : 테이블 스키마(뼈대)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")

# 1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")

# 입력 파라메터 처리(python format {0}, {1})
# 텍스트 박스(GUI, Web Page)에서 입력을 받아서 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

# 다중의 레코드(행, row)를 입력받는 경우 : 2차원 행열 데이터
datalist = (("tom", "010-123"), ("dsp", "010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

# 검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

# 1건 검색
print( cur.fetchone() ) # 1개 출력 --> np

# N건 검색
print("---fetchMany(2)---") # 2개 출력 --> np
print( cur.fetchmany(2) )

print("---fetchAll()---") # 전체 출력인데 1개 나옴 ==> 버퍼에 남은 데이터가 1개라서
cur.execute("select * from PhoneBook;") # 이거 추가하면 다시 버퍼 데이터 
#리셋 돼서 정상 출력
print( cur.fetchall() )

# 결과를 슬라이싱
cur.execute("select * from PhoneBook;")
result = cur.fetchone()
print(result[0])
print(result[1])

# 2차원 행열 데이터 [행][열]
print("---다중 행의 경우---")
result = cur.fetchall()
print(result[0][0])
print(result[0][1])