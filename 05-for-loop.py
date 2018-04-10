# for, range
# while

# for
# 1부터 10의 숫자를 하나씩 꺼내어 처리
# range(1:10)이지만 출력은 1에서 9까지만 (마지막 숫자는 출력 x)
# for 구문은 list, tuple, set 같은 목록의 형태를 다 받을 수 있다.

for num in range(1,10): # cf. [1,2,3] [0:2]
    print(num)

num_list = [1,2,3,4,5,6,7,8,9]
for num in num_list:
    print(num)

# while
# if와 for가 결합된 형태
while True: #무한루프
    print(1)

a = 1
while a <10:
    print(a)
    a = a +1  # =표시가 하나 있을때는 '할당'

# [정리]
# for는 range와 함께 사용
# 또는 list, tuple, set, dict의 목록의 형태와 함께 사용
# while은 항상 그 다음에 조건을 받게 됨
# 조건이 True에서 False로 바뀔 때 무한루프가 종료됨
