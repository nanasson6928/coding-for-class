# 미니 과제 1. 랜덤 뽑기
# •개발자에게 필수적인 구글 검색(구글링) 능력을 키워봅시다.
# •리스트나 튜플에서 임의로 하나의 값을 뽑으려면 어떻게 해야할까요?
# •[1, 2, 3, 4, 5] 라는 리스트 중에 임의의 값을 하나 뽑아주세요.

# 힌트
# •검색 키워드: python, random, random.choice, random.randint
#--------------------------------------------------------------
import random
num_list = [1,2,3,4,5]
print(random.choice(num_list))

# 참고 링크
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

# import random : random 이라는 명령어를 저장
# random.choice(num_list) : num_list를 랜덤으로 뽑기
