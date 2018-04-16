# <구현 내용>
# - 앞서 중간 점검 때 공부했던 구구단이 사용자가 어떤 다른 값을 넣더라도 에러가 나지 않도록 처리해 봅시다.
#   (추가 과제에서 2~9라는 숫자 외에는 구구단이 출력하지 않도록 처리했습니다.)
# - 예를 들어, 현재 숫자가 아닌 "1단"이라는 문자를 넣으면 구구단이 실행되지 않고 종료됩니다.
# - 잘못된 값을 입력한 경우, "2에서 9사이의 숫자만 입력해주세요."이라는 문구와 함께 다시 구구단이 실행되도록 합시다.
#
# <힌트>
# - 에러 처리를 이용합니다.
# - 함수 안에 동일한 함수를 다시 호출할 수 있습니다. 검색 키워드: 재귀 함수

dan = int(input("2에서 9사이의 숫자를 입력해주세요 : "))
# - input은 문자로만 받으므로 int로 감싸주기
#   (숫자로 입력해도 문자로 답해줘야 함)

for num in range(1, 10): # 1에서 9까지의 num 나열
    print("{} * {} = {}".format(dan, num, dan * num))

# ! 그런데 1을 넣어도 계산이 진행됨
#   - dan = 2에서 9까지, num = 1 ~ 9 까지로 정의했는데도
#   - 10 넘는 수를 입력해도 계산이 진행

# ! '1단'을 입력하면,
# ValueError: invalid literal for int() with base 10: '1단'

# --> 함수 이용
#  - 2~9 이외의 숫자를 입력할 경우 예외로 처리하기
#  - try : 이후에 문제가 발생할지도 모르는 부분의 statement 포함
#  - except : 이후에 문제가 발생했을 때 알림 메세지 포함

def gugudan():
    try:
        dan = int(input("2에서 9사이의 숫자를 입력해주세요 : "))
        for num in range(1, 10):
            print("{} * {} = {}".format(dan, num, dan * num))

    except ValueError:
        print("숫자만 입력해주세요.")

# --> 에러 안내 메세지가 뜨지만 바로 종료됨. 다시 실행해야함
# --> 재귀함수 사용 : 함수 안에서 다시 함수 쓰기
# - try문을 읽다가 오류 남 ('1단' 입력)
# - 자동으로 except문으로 넘어옴
# - 안내 메세지 출력 후 다시 함수 호출

def gugudan():
    try:
        dan = int(input("2에서 9사이의 숫자를 입력해주세요 : "))
        for num in range(1, 10):
            print("{} * {} = {}".format(dan, num, dan * num))
    except ValueError:
        print("숫자만 입력해주세요.")
        gugudan()
    except : # ValueError말고 다른 에러 발생했을 경우
        print("알 수 없는 에러가 발생했습니다.")
gugudan() # 함수 실행


# 조건 추가
def gugudan():
    try:
        dan = int(input("2에서 9사이의 숫자를 입력해주세요 : "))
        if dan > 1 and dan < 10:
            for num in range(1, 10):
                print("{} * {} = {}".format(dan, num, dan * num))
        else:
            print("2에서 9사이의 숫자만 입력해주세요!!")
            gugudan()
    except ValueError:
        print("숫자만 입력해주세요.")
        gugudan()
    except : # ValueError말고 다른 에러 발생했을 경우
        print("알 수 없는 에러가 발생했습니다.")
gugudan()
