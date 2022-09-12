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

