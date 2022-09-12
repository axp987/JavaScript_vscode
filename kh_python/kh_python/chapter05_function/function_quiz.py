#끝말잇기 함수 만들기
def game(text):
    print("차표")
    while True:
        next = input("끝말을 이어주세요> ")
        if text[-1] != next[0]:
            print("끝말이 이어지지 않습니다.")
            break
        else:
            text = next
            print(next)

game("차표")