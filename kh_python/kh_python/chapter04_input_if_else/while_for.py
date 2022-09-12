"""""
num = 0

while num < 5:
    num += 1
    print(num)
"""""

fruits = ["사과", "키위", "바나나", "사과", "바나나", "망고"]
print(fruits)
rFruit = input("빼낼 과일을 말해주세요: ")

while rFruit in fruits: # in은 만약에 라는뜻으로 fruits 안에 rFruit이 있다면 반복해라
    fruits.remove(rFruit) # 고로 앞에 사과 뒤에 사과 둘 다 없어짐

print(fruits)
print("{}를 모두 제거했습니다.".format(rFruit))





