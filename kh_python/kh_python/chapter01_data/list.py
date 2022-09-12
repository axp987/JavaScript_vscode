#items[start:stop]  # 리스트의 start 인덱스에서 stop-1 인덱스까지 슬라이싱
#items[start:]      # 리스트의 start 인덱스에서 리스트의 마지막까지 슬라이싱
#items[:stop]       # 리스트의 처음부터 stop-1 인덱스까지 슬라이싱
#items[:]           # 리스트 전체 아이템들 반환(복사본)

#items[start:stop:step]
#items[2:9:3] # 인덱스 2에서 인텍스 9까지(인덱스 9는 제외) 3칸씩 점프 
# [2, 5, 8]

#items[:10:2] # 처음부터 인텍스 10까지(인덱스 10은 제외) 2칸씩 점프
# [0, 2, 4, 6, 8]

#items[2::2] # 인덱스 2에서 끝까지 2칸씩 점프
# [2, 4, 6, 8, 10]

#items[::3] # 전체 리스트에 대해서 3칸씩 점프
# [0, 3, 6, 9]

fruit1 = ["banana"]
fruit2 = ["apple"]

print(fruit1 > fruit2)

td_number = [[10,20,30],[1,2,3]] # 10 20 30
print(td_number[0][1])           # 1  2  3 이런식으로 표현됨 자바랑은 다름