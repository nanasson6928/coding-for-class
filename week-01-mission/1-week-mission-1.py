# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.
# 리스트를 여러 개 사용하고 사용자의 입력을 받아야 합니다.

# food = input("한식, 중식, 일식 중 한 가지를 고르세요")
# food_list = ["한식","중식","일식"]
# restaurant = ["김밥천국","홍콩반점","역전우동"]
#
# import random
# print(random.choice(restaurant))

## [정답] ##
# - 리스트를 여러 개 사용하고 사용자의 입력을 받아야 한다.
# - 리스트에서 데이터를 임의로 하나를 뽑는 방법은 2가지
# - 그 중 아무거나 사용해도 됨 (구글링)
# - 모든 것을 아는 개발자는 없음
# - 따라서 검색 능력도 개발자에게 꼭 필요함
# - 검색 키워드 : random, randint, shuffle, choice

import random

# 1) 리스트를 만든다.
KOREAN_FOOD = ("김치찌개","비빔밥","국수")
CHINESE_FOOD = ("짜장면","탕수육","짬뽕")
JAPANESE_FOOD = ("라멘", "돈까스", "돈부리")

# 2) 사용자로부터 입력을 받는다.
user_choice = input("한식, 중식, 일식 중에서 골라주세요 :")

# 3) 임의로 추천
if user_choice == "한식":
    choice_result = random.choice(KOREAN_FOOD)
elif user_choice == "중식":
    choice_result = random.choice(CHINESE_FOOD)
elif user_choice == "일식":
    choice_result = random.choice(JAPANESE_FOOD)
else: # 다른 값을 입력할 경우... pass 써도 됨
    print("한식, 중식, 일식 중에서 선택하셔야 합니다.")

if choice_result :
    print("{} 중에서 {}(이)가 선택되었습니다.".format(user_choice, choice_result))
# - choice_result에 값이 담겨있을 경우, print()
#   user_choice와 choice_result에 맞게
# - user_choice : input 질문의 결과
# - choice_result : random.choice(KOREAN/CHINISE/JAPANESE_FOOD)

# <random.randint 사용>
# 만약 KOREAN_FOOD 자료형이 integer라면,
# if user_choice == "한식":
#     choice_result = KOREAN_FOOD(
#         random.randint(0, len(KOREAN_FOOD))
#     )
# - len : 리스트의 길이 반환
#   [1,2,3]면 index 0,1,2
