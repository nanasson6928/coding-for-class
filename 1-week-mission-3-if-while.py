# <구현 내용>
# - 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# - 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# - 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.
#
# <힌트>
# - 리스트를 한 개를 사용하고 사용자의 입력을 받아야 합니다.
# - 앞서 사용했던 임의 뽑기를 다시 사용합니다. 검색 키워드 : random, randint, shuffle
# - 컴퓨터에게 가위, 바위, 보의 승패를 가르쳐줘야 합니다.

SCISSORS = "가위"
ROCK = "바위"
PAPER = "보"

RSP_LIST = (
    ROCK,
    SCISSORS,
    PAPER
)

import random

# 변수를 미리 만들어 놓는 이유 #
# - 코드 작성 시, 잘못 쓸 경우가 있기 때문에 변수로 미리 정의해놓는게 편리.

win_count = 0
lose_count = 0

# 무한 루프 : 사용자 - 컴퓨터 간 가위바위보 --> 3번을 지거나 이기면 종료
while win_count <3 and lose_count <3:
# (-> while 구문은 True가 False가 될 때 반복을 멈춘다.)
# 1) 사용자 입력 - 가위, 바위, 보 묻기
    user_choice = input("{}, {}, {} : ".format(
        SCISSORS, ROCK, PAPER
    ))
# 2) 컴퓨터 임의 선택 - 가위, 바위, 보 중 하나 선택하기
    computer_choice = random.choice(RSP_LIST)
    if user_choice == computer_choice:
        print("비겼습니다.")
# 4) 가위, 바위, 보 만 입력하도록 함
    elif user_choice not in RSP_LIST:
        print("가위, 바위, 보 중 하나를 입력해주세요.")
# 3) 승패 결정
    elif ((user_choice == ROCK and computer_choice == SCISSORS)
        or(user_choice == SCISSORS and computer_choice == PAPER)
        or(user_choice == PAPER and computer_choice == ROCK)):
        win_count = win_count + 1
        print("이겼습니다.")
    else:
        lose_count = lose_count + 1
        print("졌습니다.")
