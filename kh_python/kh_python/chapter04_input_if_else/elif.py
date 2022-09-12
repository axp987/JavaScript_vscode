"""""
odd = input("주민등록번호 뒷자리를 입력하세요: ")
inNum = int(odd[0])
 # 홀수 , 짝수 구별

if (inNum % 2 == 1): {
    print("남성 입니다.")
}
elif(inNum % 2 == 0): {
    print("여성 입니다.")
}
else:
    print("잘못입력하셨습니다.")
"""""   

number = int(input("3의 배수이면서 짝수를 판별해드려요: "))

if number % 3 == 0 and number % 2 != 0:
    print("3의 배수입니다.")
elif number % 3 == 0 and number % 2 == 0:
    print("3의 배수이면서 짝수 입니다.")
else:
    print("3의 배수도 짝수도 아닙니다.")