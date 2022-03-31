# DemoForm2.py
# DemoForm2.ui(화면) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹서버와 통신할 경우 사용
import urllib.request
#크롤링에 사용
from bs4 import BeautifulSoup
#디자인 파일 로딩

form_class = uic.loadUiType("c:\\work\\DemoForm2.ui")[0]

#클래스 정의(QMainWindow클래스 상속) : 다중상속은 C++, Python정도만 허용
class DemoForm(QMainWindow, form_class):
    #초기화 메서드(self, this, super, base)
    # 상속시에는 부모의 초기화를 부르도록 한다.(부모쪽 초기화 위해) : super
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")
    #슬롯메서드 정의
    def firstClick(self):
        f = open("c:\\work\\webtoon.txt", "a+", encoding="utf-8")
        data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
        soup = BeautifulSoup(data, "html.parser")
        cartoons = soup.find_all('td', class_='title')
        for item in cartoons:
            title = item.find('a').text
            print(title)
            f.write(title + "\n")

        self.label.setText("네이버 웹툰 리스트")
        f.close()
    def secondClick(self):
        self.label.setText("두번쨰 버튼")
    def thirdClick(self):
        self.label.setText("세번쨰 버튼")


#진입점 체크 : 직접 이 모듈을 실행한 경우는 프로세스를 만들고 창을 보여준다.
#C언어는 main()함수가 진입점(Entry Point)
if __name__ == "__main__":
    #실행프로세스(Excel.exe)
    app = QApplication(sys.argv)
    #인스턴스 생성
    demoWindow = DemoForm()
    #show()메서드
    demoWindow .show()
    #이벤트 루프(이벤트 발생 대기)
    app.exec_()