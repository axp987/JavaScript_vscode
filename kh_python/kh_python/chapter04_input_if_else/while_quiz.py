#최소값 최대값 입력 받고 그 사이에 있는 홀수 짝수 리스트에 담아서 안에 있는 숫자 출력
min_num = int(input("최소값 입력: "))
max_num = int(input("최대값 입력: "))

#홀수, 짝수 리스트 생성
odd = []
even = []

num = min_num

if min_num < max_num:
    while num < max_num:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
        num += 1
    print("{}부터 {}까지의 짝수는 {}입니다.".format(min_num, max_num, even))
    print("{}부터 {}까지의 홀수는 {}입니다.".format(min_num, max_num, odd))
else:
    print("최대값 {}이 최솟값 {}보다 크지 않습니다".format(max_num, min_num))