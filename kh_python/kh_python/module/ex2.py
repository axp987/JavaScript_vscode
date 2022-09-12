from datetime import datetime, timedelta

#import date
#today = date.today()
#print(today)
#new_date = date(1999, 12, 31)
#print(new_date)

#import time
#print(time(9))
#print(time(9, 2))
#print(time(9, 2, 2))
#print(time(9, 2, 2, 2222))

#import datetime
#dt = datetime.now() #현재날짜, 시각
#dt = datetime(2002, 10, 20, 14, 5, 2)
                #년 월 일 시간 분 초

#import datetime, timedelta #날짜와 시간의 차이를 계산해줌
#today = datetime.now()
#print(today +  timedelta(days=20))

from time import strftime
now = strftime("%Y-%m-%d %H:%M")
print(now)

#pypi 파이썬 라이브러리
#pip install Django==2.0
#pip uninstall Django==2.0