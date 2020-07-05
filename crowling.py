#Beautifulsoup 패키지 설치
#pip install bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen

#결과를 저장할 파일 생성
f = open("검색어 순위.txt", 'w')
#크롤링해올 url 오픈 및 이름을 response로 저장 
with urlopen('https://search.naver.com/search.naver?sm=top_sug.pre&fbm=1&acr=3&acq=%EA%B2%80%EC%83%89%EC%96%B4&qdt=0&ie=utf8&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EC%8B%A4%EC%8B%9C%EA%B0%84+%EA%B2%80%EC%83%89%EC%96%B4+%EC%88%9C%EC%9C%84') as response:
    #url의 html을 파싱
    soup = BeautifulSoup(response, 'html.parser')
    #grade를 1로 초기화
    grade = int(1)
    #span class = "tit"인 부분을 select
    for anchor in soup.select("span.tit"):
        #결과를 파일에 저장
        data ="%d위: %s" %(grade, anchor.get_text())
        f.write(data)
        # grade의 값을 올리기(미실행시 span.tit에 해당하는 첫 데이터만 저장됨)
        grade = grade + 1
#파일        
f.close()

