#try: > 예외가 발생할 가능성이 있는 코드
#except: > 예외가 발생했을 때 실행할 코드
#예외가 어디서 발생할지 신중히 잘 생각하기
"""""
def div():
    try:
        num1 = input("정수를 입력해주세요: ")
        num2 = input("정수를 입력해주세요: ")
        
        return print(f"{num1}을 {num2}로 나눈 값은 {int(num1) / int(num2)}입니다.")
    except :
        print("0이 아닌 숫자로된 정수로 입력해주세요.")
"""""
def div():
    try:
        num1 = int(input("정수를 입력해주세요: "))
        num2 = int(input("정수를 입력해주세요: "))
        
        #return print(f"{num1}을 {num2}로 나눈 값은 {int(num1) / int(num2)}입니다.")
        result = num1 / num2
    except Exception: # BaseException
        print("오류 발생!!")
    #except ValueError:
    #    print("숫자로 된 정수를 입력해주세요")
    #except ZeroDivisionError:
    #    print("0을 입력하지 말아주세요")
    #except KeyboardInterrupt:
    #    print("종료하셨습니다.")
    #finally: #이 구문을 사용하면 무조건 실행됨
    #    print("정상적으로 나누기 함수가 호출 되었습니다.")
    else:
        print("정상적으로 나누기 함수가 호출 되었습니다.")
        return print(f"{num1}을 {num2}로 나눈 값은 {result}입니다.")

div()
#help(ZeroDivisionError)