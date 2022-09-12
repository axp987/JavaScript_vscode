#최대, 최소값 구하기
"""""
def sorts(max_min_search):
    max = 0
    min = 100
    for i in max_min_search:
        if max < i:
            max = i
        elif min > i:
            min = i
    return max, min
"""""
def max_min_search(*number):
    max = number[0]
    min = number[0]
    for num in number:
        if max < num:
            max = num
        elif min > num:
            min = num
    return max, min

print(max_min_search(15, 30, 4, 60, 7, 80, 32))
