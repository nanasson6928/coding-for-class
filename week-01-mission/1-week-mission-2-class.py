# <구현 내용>
# •사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# •직장 동료 클래스를 사람 클래스를 이용해서 만듭시다.
#  사람 기본 요소 외 별도의 추가 사항은 직급입니다.

# <힌트>
# 클래스와 상속을 활용합니다.
# 사람의 기본 요소인 이름, 나이, 성별은 각각 새로운 사람을 만들 때, 입력을 받을 수 있도록 합시다.
# 직장 동료의 기본 직급은 "대리"로 지정합니다.
# (고급) 사람 클래스에서 새로운 사람을 만들 때 입력은 그대로 유지하면서,
# 직급도 처음 만들어질 때 입력하도록 변경을 도전해봅시다.

# 1) 사람 클래스
class Person:
    # 이름, 나이, 성별
    # name, age, gender
    # 1-1) 새로 만들 때 입력(name, age, gender)
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
# 2) 직장 동료 클래스
# 상속
class Colleague(Person):
    # 2-1) 기본 직급 대리
    # position = "대리" --> 기본 변수로 입력
# 2-2) 새로 만들 때 입력
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position

colleague = Colleague("nanasson",29,"Female","대리")
print(colleague.name)
print(colleague.__dict__)
