"""""
i = 0
while True:
    num = int(input("정수를 입력해주세요 (0입력시 종료): "))
    if num == 0:
        break
    i += num
    print("현재 정수의 합은 {}입니다.".format(i))
else:
    print("종료되었습니다") #break문에 의해 실행되지 않음
print("최종 정수의 합은 {}입니다.".format(i))
"""""
numbers1 = [10, 200, 30, 400, 50]

for i in numbers1:
    if i < 200:
        continue
    #print("{}은 200이상의 숫자입니다.".format(i))

numbers2 = [[1,2,3],[10,20,30]]

for i in numbers2:
    print(i)
    for j in i:
        print(j)
        break
