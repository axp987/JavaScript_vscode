# requests 파이썬에서 라이브러리에 요청한다는 뜻
# pip install requests 콘솔창에서 다운로드
# BeautifulSoup 을 이용하여 파싱함(문법적인 구성으로 맞게 보여줌)
# pip install BeautifulSoup4 콘솔창에서 다운로드
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com")

#content는 원시값을 보여줌(16비트로 만들어진 기본값)
#print(r.content)
#text는 html 형식으로 보여줌
#print(r.text)


# BeautifulSoup으로 훨씬 더 보기 편하게 바꿔줌
bs = BeautifulSoup(r.content, "html.parser")
#print(bs)
bs1 = bs.select("h3") # h3들의 요소들을 반환해줌
bs2 = bs.select_one("h3 > a") # h3들 중 가장 첫번째 요소를 반환해줌
#print(bs1[1].text) # h3에 적혀있는 요소를 보여줌 #one은 배열 없이 호출
#print(bs1[0].attrs) # 태그의 속성과 값을 호출함
#print(bs2) # <a href="https://www.naver.com/NOTICE">공지사항</a> # > a를 하면 이런식으로 출력해줌


# div는 별명을 설정 시켜주는거 <div> </div>의 자식 요소들을 출력 시켜줌
bs3 = bs.select_one("div.current_box")
#print(bs3)


bs4 = bs.select(".title") # title의 모든 결과를 출력
#print(bs4)

selecter = bs.find("div", {"class":"partner_box"}) # find_all("태그명", {"속성명":"속성값"})
#selecter = bs.find_all("div", {"class":"partner_box"}) # find_all("태그명", {"속성명":"속성값"})
#print(selecter)
#print(selecter.text)