# 참과 거짓 boolean
# if
# True, False
# and, or, # NOT

a = True
b = False
# A가 참이고, 그리고 B가 참이라면 (A와 B가 둘 다 참이어야 한다.)
print(a and b)
# A가 참이거나 혹은 B가 참이라면, (A나 B 둘 중에 하나라도 참이면 된다.)
print(a or b)

# = & ==
a = True # a에 True 할당
a == True # a와 True가 같은가
print(a == True) # a와 True가 같니?
print(a is True) # a는 True니?

# if :
# elif : 조건이 여러 개로 중첩될 때
# else : 해당 조건이 아무것도 일치하지 않을  :
d = 7
if d >10:
    print("숫자는 10보다 큽니다")
elif d > 5 and d <= 10:
    print("숫자는 10보다 작거나 같고, 5보다는 큽니다")
else :
    print("숫자는 5보다 작거나 같습니다")

# 정리 #
# 참과 거짓 boolean
# 참과 거짓을 and/or의 방법을 통해서 서로 연산
# a가 참이고 b가 참이라는 조건을 검사할 수 있다는 뜻
# 해당 검사의 내용을 if, elif, else를 통해 표현
