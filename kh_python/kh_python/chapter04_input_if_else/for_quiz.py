#구구단
"""""
for i in range(2, 10):
    print("======= {}단 =======".format(i))
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j))
"""""
"""""
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(f"{i} * {j} = {i*j}", end = "\t")
    print()
"""""
"""""
#다차원 리스트
list_3rd = [[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]]
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in list_3rd: #123456 123 1 2 3 > 456 4 5 6
    cnt1 += 1 
    print("i의 {}번째 반복입니다.".format(cnt1))
    print(i)
    for j in i:
        cnt2 += 1
        print("j의 {}번째 반복입니다.".format(cnt2))
        print(j)
        for k in j:
            cnt3 += 1
            print("k의 {}번째 반복입니다.".format(cnt3))
            print(k)
print("i는 {}반복, j는 {}반복, k는 {}반복".format(cnt1,cnt2,cnt3))
#i는 큰들(2번) j는 중간틀(4번) k는 1개씩 전부 다(12번)
"""""
"""""
menu = {
    "아이스 아메리카노": 3000,
    "아이스라떼": 4000,
    "아이스크림": 8000,
    "아메리카노": 2500,
    "라떼": 3500
}

ice_menu = {}
hot_menu = {}

#print("제품명: {}, 가격: {}".format(i, j))    
for i, j in menu.items():
    #if i.find("아이스"): # find는 참인거는 False(0)을 반환 / 거짓은 True(1) 반환
        #print(i, j)
    #else:
        #print(i, j)

    if i[0:3] == "아이스":
        ice_menu[i] = j
    else:
        hot_menu[i] = j

print("차가운 메뉴")
for i, j in ice_menu.items():
    print("제품명: {}, 가격: {}".format(i, j))
print("뜨거운 메뉴")
for i, j in hot_menu.items():
    print("제품명: {}, 가격: {}".format(i, j))
"""""

num = int(input("N의 값을 입력하세요: "))
print("N의 값 : ", num)
result = 0
for i in range(1, num+1):
    if i % 2 == 0:
        result += i ** (i-1)
print("합계: {}".format(result))
    
            