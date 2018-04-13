
name1 = "성안고"
foundation = 1999
address = "경기도 안산시 상록구 용신로 170"

name2 = "상록고"
foundation2 = 2013
address2 = "경기도 안산시 상록구 반석로4길 34"

name3 = "동산고"
foundation3 = 1994
address3 = "경기도 안산시 상록구 충장로 56"


class School:
# __init__을 사용하면 class 생성 뒤 변수를 따로 만들지 않아도 됨
# School을 새로 생성할 때 마다 name,foundation,address를 입력하도록 함
    def __init__(self, name, foundation, address):
        self.name = name
        self.foundation = foundation
        self.address = address



school1 = School("성안고",1999,"경기도 안산시 상록구 용신로 170")
school2 = School("상록고",2013,"경기도 안산시 상록구 반석로4길 34")
school3 = School("동산고",1994, "경기도 안산시 상록구 충장로 56")

print(school1.name)
print(school1.foundation)
print(school1.address)
