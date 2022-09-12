
web = input("웹사이트 주소를 입력해주세요: ")
word = web.split(".") #("@") 기준으로 배열로 나눔 ['www', 'naver', 'com']

if word[-1] == "kr":
    print("한국")
elif word[-1] == "uk":
    print("영국")
elif word[-1] == "com":
    print("기업용")
elif word[-1] == "org":
    print("기관")
else:
    print("알 수 없음")

"""""
if con == ".kr":
    print("한국")
elif con == ".uk":
    print("영국")
elif con == "com":
    print("기업용")
elif con == "org":
    print("기관")
else:
    print("알 수 없음")
"""""
