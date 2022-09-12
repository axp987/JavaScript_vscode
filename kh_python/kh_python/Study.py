#포맷, 리스트, 튜플, 딕셔너리, 함수

#1. 포맷###########################
left = "left"
right = "right"
middle = "middle"

# <>^ 왼쪽정렬, 오른쪽정렬, 가운데정렬
# 10은 총길이 (left는 4글자이니 6개의 공백이 남음)
# 맨뒤에 .(숫자)s를 입력하면 짜르기
print("({0:!>10.4s}), ({2:@^10.3s}), ({1:#<10.2s})".format(left, right, middle))

#f-string
print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도 입니다.")
print(f"2곱하기 30의 결과값은 {2*30}")

#2. 리스트###########################
fruit1 = ["banana"]
fruit2 = ["apple"]

print(fruit1 > fruit2)

td_number = [[10,20,30],[1,2,3]] # 10 20 30
print(td_number[0][1])           # 1  2  3 이런식으로 표현됨 자바랑은 다름

#3. 튜플###################################
# #배열과는 좀 다른건가
numbers = 1, 2, 3, 4


number0 = numbers[0]
number1 = numbers[1]
number2 = numbers[2]
#number0, number1, *number2 = numbers # *을 쓰면 나머지를 number2에 담겠다 의미

print(id(numbers))

numbers += 5, 6
print(numbers)
print(id(numbers))

#4. 딕셔너리###############################
#dictionary
#{
# "Daniel ping" : "파는것이 인간이다," "Eric Schmidt" : "새로운 디지털 시대"
#}      키                 값

people = {
    #키: 값
    "name": "김개똥",
    "phone": "010-1010-2020"
}
#print(people["name"])

books = { 
    "Daniel ping": ["파는것이 인간이다", "언제할 것인가"], 
    "Eric Schmidt": "새로운 디지털 시대" 
}
#print(books["Daniel ping"])

test = {
    1:"one",
    True:"True"
} #키값이 논리형(true, false)일때는 1과 0은 같은 값으로 간주하기 때문에 피해주자
#print(test[1])

coffee = {
    "Java": 2500,
    "Americano": 2500,
    "Latte": 3000
}
#coffee["Java"] = 3000 #변경
#coffee["Moca"] = 3500 #추가
#del coffee["Java"] #삭제

#print(coffee["Java"]) #확인 방법1
#print(coffee.get("Java")) #get 메소드 이용
print(coffee.keys()) #keys 메소드를 이용하여 전체키 출력(메뉴)
print(coffee.values()) #values 메소드를 이용하여 전체요소 출력(가격)
print(coffee.items()) #키와 값을 튜플로 반환 해줌

#5 집합################################
#집합 (랜덤 출력?)
# Add 123, "문자", True, ("튜플")은 추가가능
# 일반적으로는 [1, 2, ,3] list나 { keys:value } 딕셔너리는 추가 불가능
# update 메소드로 추가 가능해짐 대신 키값만 출력이 가능하거나 그럼

#week = {"월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"}
#week.add("화요일")
#week.update(["일주일"], {"한달": 123})
#print(week)

#a = {0, "abc", 1}
#a.add(True)
#print(a)

#합집합
a = {1,2,3,4,5}
b = {3,4,5,6,7}
#print(a | b); print(a & b)

a.remove(4) # 지워주고 싶은 원소를 적으면됨 / 배열 아니다
# 신기한게.... True, False로 1, 0을 지울수 있음.... 나중에 필요할수도?
print(a)
