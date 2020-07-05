#Beautifulsoup 패키지 설치
from bs4 import BeautifulSoup
from urllib.request import urlopen


f = open("검색어 순위.txt", 'w')
with urlopen('https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=3&acq=%EA%B2%80%EC%83%89%EC%96%B4&qdt=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84') as response:
    soup = BeautifulSoup(response, 'html.parser')
    grade = int(1)
    for anchor in soup.select("span.tit"):
        data ="%d위: %s" %(grade, anchor.get_text())

        f.write(data)
        print("%d위: %s" %(grade, anchor.get_text()))
        grade = grade + 1
f.close()

