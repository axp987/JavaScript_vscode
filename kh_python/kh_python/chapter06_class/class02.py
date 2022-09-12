# int(), str(), float(), bool(), tuple().... type()
# 애내들 등등 클래스임

text = 'a'
# 1 = 데이터 int 인스턴스(객체)
number = 1
a=1.0
# id() = 객체의 주소값을 반환
#print(id(number))
#print(id(a))
#print(id(1)) # 모두 id의 주소값은 같은 객체이다

print(isinstance(number, int)) # 1 True
print(isinstance(a, int)) # 1.0 False

text1 = 12345
text2 = "12345"

print(id(text1), id(text2))
print(id(text1), id(int(text2)))