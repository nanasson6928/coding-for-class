# [구구단 만들기]

# 1. 사용자로부터 몇 단을 출력할 지 받을 것
# 2. 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

# dan = input("몇 단을 출력하시겠습니까?")
# input의 경우 사용자가 숫자를 입력하더라도 문자로 변환시켜 데이터를 담음
# 숫자로 변환시키기 위해 int()에 담기
dan = int(input("몇 단을 출력하시겠습니까?"))
for num in range(1,10): #마지막 숫자 생략 --> 1~9
    print("{}".format(dan * num))

# 임의의 문자열 "{}" 만든 후
# format안에 들어가는 숫자를 빈 공간에 넣기

for num in range(1,10):
    print("{} * {} = {}".format(dan, num, dan * num))

# "{} * {} = {}"
# 문자열 속에는 총 3가지의 값을 후에 임의로 넣어줌
# n * n = n 의 방식

# format(dan, num, dan * num)
# 만들어 놓은 문자열을 format에 활용하겠다는 의미
# 중괄호를 이용해서 빈 칸을 만들어 놓은 부분에
# format 안 변수의 순서대로 결과값을 중괄호에 각각 넣어줌