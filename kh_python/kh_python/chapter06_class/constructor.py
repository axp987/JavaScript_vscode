class BreadMold:
    category = "빵"
    price = 2000
    #동작 방식을 바꿔야만 할때 __ @@ __ 사용
    def __init__(self, category, price): 
        # __init__은 초기화를 의미이며 self는 자바의 this 의미
        self.category = category
        self.price = price
        print("빵을 만들었습니다.")

    def __str__(self):
        ''' '''
        return "첫번째 빵의 제품은 {}이고, 가격은 {}원 입니다.".format(bread1.category, bread1.price)

    def __del__(self):
        print("빵을 그만 만듭니다.")

#변수는 객체를 가르키고 있는 이름표
# _init_ 생성자 메소드
#bread1는 객체가 아닌 객체를 참조하는 이름
bread1 = BreadMold("단팥빵", 3000)
bread1 = BreadMold("원빵", 1000)
#print("첫번째 빵의 제품은 {}이고, 가격은 {}원 입니다.".format(bread1.category, bread1.price))
# 17행을 만들고 레퍼런스 카운터가 0이됨
# 그리고 18행을 새롭게 참조하게 됨
# 그다음 __del__인 소멸자 메소드가 실행이됨
# 18행도 소멸자가 동작함
print(bread1)

