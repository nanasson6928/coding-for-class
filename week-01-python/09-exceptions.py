# exceptions

# ZeroDivisionError: division by zero
# - 1/0
# - 수학적으로, 0으로 나누면 무한대로 가버림
# - 프로그래밍에서도 에러

# 나누기 함수 만들기
# def  divide_by(first, second): # 1번 인자와 2번 인자를 받고
#     return first / second      # 1번 인자를 2번 인자로 나눔

# print(divide_by(4, 2))         #  4/2
# print(divide_by(4, 0))         #  error

# 사용자는 생각하지 못한 곳에서 에러를 냄
# 에러를 잡아 줄 필요가 있음 --> try (예약어)
def divide_by(first, second):
    try:
        return first / second
    # except + 에러 이름
    except ZeroDivisionError :
        return "0으로 나눌 수 없습니다."

print(divide_by(4, 2))
print(divide_by(4, 0))


# 예외 만들기
# Exception class
# class의 '상속'을 이용

# - Exception 클래스 생성
# 1. divide_by_odd_number 함수 생성
# 2. second를 2(짝수)로 나눠 1이 나오면 EvenNumberDevisionError
# 3. else --> first를 second로 나눈 값 반환
class EvenNumberDevisionError(Exception):
    pass
def devide_by_odd_number(first, second):
     if second % 2 == 0:
         raise EvenNumberDevisionError
     else:
         return first / second

print(divide_by_odd_number(6, 3))
print(divide_by_odd_number(6, 2))
