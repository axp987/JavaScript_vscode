# raise는 사용자가 직접 오류를 일으켜 예외처리를 해주는 방법
# 화장실이 너무 급한 남자
class toilet:
    def __init__(self): #생성자
        self.using = False

    def in_use(self):
        if self.using == False:
            print("화장실을 사용합니다.")
            self.using == True
        else:
            raise Exception("안에 사람이 있어요!! 잠시 기다려주세요")

    def not_in_use(self):
        self.using == False
        print("안에 사람이 없습니다.")

man = toilet()

while True:
    use = input("화장실을 사용하시겠습니까?(y/n) > ")
    try:
        if use == "y":
            man.in_use()
        else:
            man.not_in_use()
    except BaseException as e:        
        print(e)