# pip install pandas 엑셀처럼 행,열을 지정해주는 라이브러리
# pip install openpyxl 엑셀로 넘겨주는 라이브러리
import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://news.google.com/search?q=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

#기사제목, 링크
seoul = bs.select("div.xrnccd > article > h3 > a")

news = []

for i in seoul:
    title = i.text
    links = "https://news.google.com" + i.get("href")[1:] # [1:0]으로 인해 com/~~~~
    news.append([title, links])
    google_news_df = pd.DataFrame(news, columns=["기사제목", "링크주소"])


google_news_df.to_excel("뉴스크롤링 결과.xlsx")
print("저장 성공!!")