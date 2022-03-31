# web2.py
#웹서버와 통신할 경우 사용
import urllib.request
#크롤링에 사용
from bs4 import BeautifulSoup

#페이징 처리

#파일로 저장
f = open("c:\\work\\webtoon.txt","wt", encoding="utf-8")

for i in range(1,6):
    url = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri&page=" + str(i)
    print(url)
    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, "html.parser")

    cartoons = soup.find_all("td", class_="title")

    for item in cartoons:
        title = item.find("a").text
        link = item.find("a")["href"]
        print(title)
        print(link)
        #title = item.text.strip()
        f.write(title + "\n")
        f.write(link + "\n")

f.close()
print("크롤링 작업 종료")