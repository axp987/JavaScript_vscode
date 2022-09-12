import requests
from bs4 import BeautifulSoup

r = requests.get("https://quasarzone.com/")
bs = BeautifulSoup(r.content, "html.parser")

#가수의 목록
#노래의 목록
music_name = []
music = bs.select("div.mid-content-area > div.right-util-wrap > div.bot-util-area > dl.list-type-a > dd > ul > li > a")

for s in range(len(music)):
    music_name.append(music[s].text)

for i in range(0, 20):
    print(f"순위 {i+1} > {music_name[i].strip()}")

#append는 추가
#len은 배열크기 반환
#<i class="rank-1">1</i>