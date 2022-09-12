# super, 부모
# sub, 자식
# 상위에서 하위는 참조 몬해

class ParentRestaurant:
    price = 15000

    def __init__(self, shopName, menu, recipe):
        self.shopName = shopName
        self.menu = menu
        self.recipe = recipe

    def __str__(self):
        return "가게 이름 {}, 메뉴는 {}이며 레시피는 {}입니다.".format(self.shopName, self.menu, self.recipe)
    
    def __del__(self):
        pass
        
class ChildRestaurant(ParentRestaurant):
    price = 20000
    #marketing = "온라인 마케팅" #재정의가 아닌 자식클래스의 객체 

    def __init__(self, name, menu, recipe, marketing): #생성자 메소드
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.marketing = marketing

    def __str__(self):
        return super().__str__() + ", 마케팅 방법: {}".format(self.marketing)

#restaurnat_info = ChildRestaurant("파이썬", "피자", "피자를 굽는다")
#print(restaurnat_info.price)
restaurnat_info = ChildRestaurant("파이썬", "피자", "피자를 굽는다", "온라인")
print(restaurnat_info)

#다른 클래스가 하위클래스를 확인하는 법
print(issubclass(ChildRestaurant, ParentRestaurant)) #True
print(issubclass(ParentRestaurant, ChildRestaurant)) #False

