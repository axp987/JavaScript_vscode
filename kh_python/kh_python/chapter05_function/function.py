# def 함수이름():
#   수행할코드

"""""
def add(num1, num2):
    '''문자열 두개(성, 이름)을 입력받아서 합쳐서 출력
        text1: 성
        text2: 이름
    '''
    print(num1 + num2)
add("홍", "길동")
"""""
def add(num1, num2):
    text = num1 + num2
    return text
print(add("홍", "길동"))