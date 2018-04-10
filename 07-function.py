# 함수 functions
# 입력값 parameters, 반환값 return

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"

# 각 사람들의 이름으로 인사
# print("hello, {}".format(name1))
# print("hello, {}".format(name2))
# print("hello, {}".format(name3))
# print("hello, {}".format(name4))
# print("hello, {}".format(name5))
# print("hello, {}".format(name6))
# print("hello, {}".format(name7))
# print("hello, {}".format(name8))

# hello를 hi로 바꾸면 8번이나 수정 작업

def hello_friends(name):
    print("hello, {}".format(name))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 함수의 구성요소로 parameters와 return 있음

# 1) 입력값 o, 반환값 o
def sum(a, b):
    return a + b

# 2) 입력값 o, 반환값 x
def hello_friends(name):
    print("hello, {}".format(name))

# 입력값 x, 반환값 o
def return_1(): # return_1이라는 함수 만들기 (입력값)
    return 1    # 1 (반환값)

# 입력값 x, 반환값 x
def hello_world():
    print("hello world")

# 반환값이 있다는 건 return이 있다는 것
# return을 한다는 의미는 변수에 담을 수 있다는 뜻.
# return 사용법
#  - num_1 = return_1()
#  - print(num_1)

# hello friends() 함수는 hello 다음에 주어지는 이름을
# print()를 이용해서 출력하는 형태
# 그러나 hello friends()는 어떤 변수에 담아도 담기지 않
