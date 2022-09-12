"""""
#객체와 인스턴스
class BreadMold:
    category = "크림빵"
    price = 3000


#객체이름 = 클래스이름()
bread = BreadMold()
bread_choco = BreadMold()
bread_choco.category = "초코크림빵"


# .은 참조연산자(.format())
print("빵 이름은 {}이며, 가격은 {}입니다.".format(bread.category, bread.price))
print(bread_choco.category, bread_choco.price)
"""""
class BreadMold:
    category = "크림빵"
    def make_bread(self): #클래스 안에 함수 생성시 인자를 전달해야되는데 self(자기자신)을 통해 사용
        print("빵을 만들어 냅니다.")

bread = BreadMold()

bread.make_bread()