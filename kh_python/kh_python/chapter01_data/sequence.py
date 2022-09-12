#list [] 안에 ,
list_a = [1, 2, 3, 4]
list_lang = ["JAVA", "C", "Ptython", "Go"]

list_lang[1:3] = ["C#", "Ruby", "js"]

#append() 리스트 맨 뒤에 제일 마지막 인덱스(-1) 수정
list_lang.append("Ruby")
print(list_lang)

#extend() 요소를 추가하는 방법
list_lang.extend([4,5,6])
#print(list_lang)

#insert(index, data) 인덱스 위치에 해당 data를 삽입한다
list_lang.insert(1, "R")
#print(list_lang)

#Pop() 제일 뒤에 있는 요소를 반환 해주고, 요소를 제거한다
#list_lang.pop(1)
#print(list_lang)

#remove("R") 해당 요소를 삭제한다.
list_lang.remove("R")
del list_lang[1] #del은 배열의 위치를 삭제
#print(list_lang)

#sort() 배열을 오름차순으로 변경 #reverse() 배열 반대편으로 정렬 (0>5 5>0)
numbers = [1000, 5000, 160, 100, 20, 3450]
name = ["홍길동", "김개똥", "이승철"]
#numbers.sort()
#numbers.reverse()
numbers.sort(reverse=True)
name.sort(reverse=False) #가나다라 순으로 정렬
print(name) 


