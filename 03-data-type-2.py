# 목록 list, tuple
# 사전 dict - dictionary
# 집합 set

list []
print("list")
list_a = [1,2,3]
print(list_a)
print(type([1,2,3]))
# index는 0부터 시작한다.
print(list_a[0])
print(list_a[1])
print(list_a[2])

# # slice (리스트를 자름)
print(list_a[0:1])
print(list_a[0:2])
#
list_a.append(4)
print(list_a)

list_a.remove(2)
print(list_a)

list_a.clear()
print(list_a)

# tuple (1,)
print("tuple")
tuple_a = (1,2,3)
print(tuple_a)
print(type((tuple_a)))
# tuple_a.append(4)은 실행 안됨
# tuple은 한 번 생성 후 내부 값 변경 불가

# dict (map)   {}
# key & value : 키와 그를 설명하는 값으로 분류
dict_a = {
"apple" : "a type of fruits",
"pen" : "a thing to write"}

print(dict_a)
print(dict_a["apple"]) # dict_a의 apple의 값을 알려달라

# edit value
dict_a["pen"] = "something to write"
print(dict_a)

# set set([])
# 일종의 집합
# list, tuple, dict과 달리 특징 없음
set_a = set([1,2,3])
set_b = set([2,4,6])
print(set_a)
print(set_b)

# 집합 - 교집합, 합집합, 차집합, 여집합
# set은 중복을 제거해준다.
# (list는 값은 값을 중복해서 넣을 수 있다.)

# 교집합
print(set_a & set_b)

# 합집합
print(set_a | set_b)

# 차집합
print(set_a - set_b)
