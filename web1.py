# web1.py
# from 패키지명 import 모듈명
from bs4 import BeautifulSoup

# 페이지를 로딩(HTML문서를 읽어와~~. 유니코드)
page = open("c:\\work2\\test01.html", "rt", encoding = "utf-8").read()
# 검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
# print( soup.prettify() )
# <p>를 모두 검색해~~ 리스트 형식으로 리턴
# print( soup.find_all("p") )
# 첫번째 <p>를 검색
# print( soup.find("p") )
# <p class = "outer-text"> 로 시작하는~ 불러오는 경우(약간의 필터링)
# print( soup.find_all("p", class_="outer-text")) # 클래스는 변수명?이 될 수 없으니까 _추가
# 특정 id속성을 검색
# print( soup.find(id="first") )
# <a>태그 가져와
# print( soup.find_all("a") )
# print( soup.find_all("b") )

# 태그를 제거하고 내부 문자열(컨텐츠만)
# <p>컨텐츠</p> 태그 필요없이 내용만 알고싶을 때
for tag in soup.find_all("p") :
    # 앞 뒤의 공백 문자를 제거
    print( tag.text.strip() ) # 태그 없이 문자열만 출력해줘







