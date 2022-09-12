# pip install pandas 엑셀처럼 행,열을 지정해주는 라이브러리
# pip install openpyxl 엑셀로 넘겨주는 라이브러리

# 웹페이지에 들어가지 않고 뉴스 검색, 기사제목, 본문, 링크, 게시물날짜 엑셀에 담아 저장
from operator import le
from turtle import left
from numpy import left_shift
import requests
from bs4 import BeautifulSoup
import pandas as pd

keyword = input("검색하고자 하는 키워드를 입력해주세요: ")
r = requests.get("https://news.google.com/searchq?q="+ keyword +"&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

#기사제목, 링크
#seoul = bs.select("div.xrnccd > article > h3 > a")
food = bs.find_all("div", {"class":"xrnccd"})

news = []

for i in food:
    title = i.find("h3").text
    links = "https://news.google.com" + i.find("a")["href"][1:]
    #description = i.find("span", {"class":"xBbh9"}).text
    maker = i.find("div", {"class":"SVJrMe"}).text
    date = i.find("time").text

    news.append([title, links, maker, date])

google_news_df = pd.DataFrame(news, columns=["기사제목", "링크주소", "신문사", "날짜"])
print(google_news_df)


google_news_df.to_excel("뉴스 검색결과.xlsx")
print("저장 완료")