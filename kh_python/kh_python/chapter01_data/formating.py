from operator import le


weather = "맑음"
temperature = 20
chance_shower = 33.5

print("오늘이 날씨는 %s 기온은 %d도 비가 내릴 확률은 %.1f%%입니다."%(weather, temperature, chance_shower))
print("오늘이 날씨는 {0} 기온은 {2}도 비가 내릴 확률은 {1}%입니다.".format(weather, temperature, chance_shower))
#.format 함수를 통해 통해 형식지정자를 자동으로 변환해줌
#중괄호 갯수와 요소(.format 안의 변수들)의 갯수가 같아야함

print("{0:}, {1:d}, {1:f}, {1:o}, {1:x}".format(weather, temperature, chance_shower))
#o는 8비트 x는 16비트?

left = "left"
right = "right"
middle = "middle"

# <>^ 왼쪽정렬, 오른쪽정렬, 가운데정렬
# 10은 총길이 (left는 4글자이니 6개의 공백이 남음)
# 맨뒤에 .(숫자)s를 입력하면 짜르기
print("({0:!>10.4s}), ({2:@^10.3s}), ({1:#<10.2s})".format(left, right, middle))

#f-string
print(f"오늘의 날씨는 {weather}이며, 기온은 {temperature}도 입니다.")
print(f"2곱하기 30의 결과값은 {2*30}")