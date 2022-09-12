#배열과는 좀 다른건가
numbers = 1, 2, 3, 4


number0 = numbers[0]
number1 = numbers[1]
number2 = numbers[2]
#number0, number1, *number2 = numbers # *을 쓰면 나머지를 number2에 담겠다 의미

print(id(numbers))

numbers += 5, 6
print(numbers)
print(id(numbers))

