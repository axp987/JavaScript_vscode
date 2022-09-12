"""""
def add(*args):
    print(args) #매개변수를 출력 (10, 20, 30, 40)
    sum = 0
    for i in args:
        sum += i
    print(sum)
add(10, 20, 30, 40)
"""""
#키워드 매개변수
"""""
def star_player(**kwargs): # **는 키워드 매개변수 의미
    for i, j in kwargs.items():
        if "서장훈" in kwargs.values():
            print("저는 LG팬임")
        else:
            print("{}는 역시 {}이지".format(i, j))
    #for i in kwargs:
    #    print(i)
star_player(축구 = "손흥민", 야구 = "박용택", 농구 = "서장훈")
"""""
from email.headerregistry import Address

#args는 ()튜플 / **kwargs는 {}딕셔너리 / list는 []임
def func_a(name, *args, address="한국", **kwargs):
    print(name, args, address, kwargs)

func_a("이호찬", "옛날", "사람", address="한양", 직업="도둑")