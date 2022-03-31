# Web1.py
from bs4 import BeautifulSoup

#문서를 로딩(문서 전체를 읽어서 문자열로 리턴) : 메서드 체인 호출
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
#전체 문서를 보기
#print(soup.prettify())

#문서에 있는 <p>태그를 전부 가져오기
#print(soup.find_all("p"))

#첫번쨰 <p>만 검색
#print(soup.find("p"))

#조건이 있는 경우:<p class="outer-text">컨텐츠</p>
#파이썬에 class 키워드와 이름충돌: class_
#print(soup.find_all("p",  class_="outer-text"))

#id를 검색해서 처리
#<p id="first">....
#print(soup.find_all(id="first"))

#태그 내부에 있는 문자열 출력 [0, 1, 2, 3]
for tag in soup.find_all("p"):
    #print(tag.text.strip())
    content = tag.text.strip()
    content = content.replace("\n", "")
    content = content.replace("\t", "")
    print(content)
