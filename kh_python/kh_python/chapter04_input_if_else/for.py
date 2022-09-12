#for "변수" in 나열가능한 자료: #list 딕셔너리 튜플 등등
    #실행할 문장


#for i in range(1, 10+1):
#    print(i)

#String도 가능
#for i in "일이십사오":
#    print(i)

"""""
# 1부터 30까지의 수 중에서 3의 배수들의 합을 구하시오
sum = 0
#for i in range(1, 30+1):
for i in range(3, 30+1, 3):
    #if i % 3 == 0:
    print("{} + {} = ".format(sum, i), end = "")
    sum += i
print(sum)
"""""
"""""
coffee = { "아메리카노": 2500, "라떼": 3000, "자바": 2000 }
for i in coffee.values():
    print(i)
"""""
"""""
fruits = ["사과", "딸기", "바나나"] #인덱스와 함께 사용할때 유용하게 사용 가능
for i in enumerate(fruits): #(0, '사과') (1, '딸기') (2, '바나나')
    print(f"{i[0]+1}번째 과일은 {i[1]}입니다.") #(0, '사과') 0은 첫번째 요소, 사과가 두번째 요소
"""""
"""""
for i in range(1, 3):
    for j in range(1, 3):
        print("첫번째 for문의 반복 {}번, 두번째 for문의 반복{}번".format(i, j))
"""""

list_2nd = [[1,2,3], ["a", "b", "c"]]

for i in list_2nd:
    print(i)
    for j in i:
        print(j)