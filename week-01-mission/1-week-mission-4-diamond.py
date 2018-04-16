# 컴퓨터 공학도의 느낌을 내보자 - 다이아몬드 그리기
# <구현 내용>
# 아래 도형을 구현 합니다.
# 00100
# 01110
# 11111
# 01110
# 00100
# 도형을 설명하면 5x5 좌표에, 다이아몬드를 그리고 있습니다.

# <힌트>
# 반복문(for-loop)을 사용

# range(5) : 0부터 4까지 출력. 0회~4회 출력 (= 5번)
# range(1, 6) : 1부터 5까지 출력. 0회~11회 출력 (= 10번)

# (ex.)
# for b in range(1, 6):
#     print(b)
# 1
# 2
# 3
# 4
# 5



# 1. 아래 내용 출력하기

# 1
# 11
# 111
# 1111
# 11111

for a in range(1, 6):
    print("1"* a )
# a : 변수, in + 조건
# range(1,6)을 변수 a에 할당
# range : 필요한 만큼의 숫자를 만들어내는 함수
# 1을 a만큼 추가해서 출력
# --> 1을 6회 추가 : 0회 ~ 5회 = 6회

# 2. 1과 0으로 다이아몬드 모양 그리기

# 1)
# 10000
# 11000
# 11100
# 11110
# 11111

for b in range (1, 6):
    print("1" * b + "0" * (5 - b))

# 1 출력은 b만큼
# 0 출력은 5 - b만큼 (1이 1번 출력 : 0은 5-1개)
# 1이 5번 출력될때까지 반복

# 2)
# 00100
# 01110
# 11111
# 01110
# 00100

for c in range (1, 6):
    c = c - 3  # 처음 시작이 0 = 4개, 1 = 1개 -> 4-1=3
    if c < 0:
        c = -c
    print("0"* c + "1"* (5 - c * 2) + "0" * c)


# (1) c = 1인 경우
#     c = 1 - 3 = -2
#     c = -(-2) = 2
#     print : 0이 2번, 1이 (5-(2*2))=1로 1번, 0이 2번 : 00100

# (2) c = 2
#     c = 2-3 = -1 < 0
#     c = -(1) = 1
#     print : 0이 1번, 1이 (5-(1*2)=3으로 3번, 0이 1번 : 01110)
