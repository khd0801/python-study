# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규표현식으로 검색
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일로 저장
f = open("c:\\work\\today.txt", "wt", encoding="utf-8")
#페이징 처리를 1번에서 10번까지
for n in range(1,11):
        #오늘의 유머 주소 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 꺠지는 경우는 디코딩이 필요
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')


# <td class="subject">
# <a href="/board/view.php?table=bestofbest&no=453480&s_no=453480&page=1" target="_top">
# 일본과 실리외교가 아주 쪄네요...</a>


        #find_all(태그, attributes(속성들))
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        tag = item.find("a")
                        title = tag.text
                        print(title)
                        f.write(title.strip() + "\n")
                        
                except:
                        pass
f.close()
print("크롤링 종료")
