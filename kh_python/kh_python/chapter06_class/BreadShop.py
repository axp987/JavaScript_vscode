class BreadMold:
    category = "빵"

#bread2의 category에 있는 이름을 찾고 그다음에 class로 와서 category의 이름을 찾음
bread1 = BreadMold()
bread2 = BreadMold()
bread3 = BreadMold()

bread1.price = 3000 # bread1의 객체 이름공간에 price를 생성
bread2.category = "붕어빵"
bread3.category = "팥빵"

print(bread1.category, bread2.category, bread3.category)
print(bread1.price)

#dir() 이름공간에 있는 모든 속성을 리스트로 반환, 메소드 객체 등등 확인 가능
print(dir(bread1))
print(dir(BreadMold))
print(dir(str))