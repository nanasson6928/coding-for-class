# 클래스 class
# 수 만 줄의 코드를 쉽게 고칠 때 쓰는 방법

### Article Variables
# 3개의 글을 변수로 표
title1 = "개발"
author1 = "마르코"
content1 = "개발은 쉬워요"
view_count1 = 0

title2 = "코칭"
author2 = "마르코"
content2 = "코칭은 쉬워요"
view_count2 = 0

title3 = "창업"
author3 = "마르코"
content3 = "창업 쉬워요"
view_count3 = 0

# 글이 3개라는 전제 하에 3개의 변수로 표현
# 만약 글이 1000개 이상으로 늘어나면 변수에 숫자 붙이기가 쉽지 않음
# [ex] 사람 1명이 글을 읽었다 (조회)
# view_count1 =1
# view_count1 =2
# view_count1 =3
# --> 불편, 귀찮음

# ##### Article class
class Article :   # Article이라는 class 만들기
    title = "개발"
    author = "마르코"
    content = "개발은 쉬워요"
    view_count = 0

# 클래스 살향
article1 = Article()
# - 클래스 이름은 보통 대문자로 시작 : Article()
# - 클래스의 설계 도면대로(변수 4개) 객체를 만들어냄
# - 클래스의 정보를 담고 있는 접근 가능한 변수를 만들어냄
# - article1이라는 변수는 Article이라는 class를 통해 만듦

print(article1.title)
# - class Article 밑으로 적어준 내용대로 출력
# - .title(변수 이름)로 접근만해도 "개발" 출력함

article2 = Article()
article2.title = "코칭"
print(article1.title) # article2가 article1에 영향 미침 여부 확인
print(article2.title)

# [중간 정리]
# - 변수 4개를 만들고 내용을 채워 class에 담기
# - article1, article2라는 변수에서 class 활성화 : Article()
# - 4줄을 1줄로 줄인 효과

##### Article Class with __init__
# author는 "마르코"로 다 같고 조회수도 같이 0으로 시작
# but, title과 content는 다른 내용으로 시작

class Article:
        author = "마르코"
        view_count = 0

        def __init__(self, title, content):  # Article을 새로 생성할 때 마다 title과 content를 입력하도록 함
            self.title = title                 # __init__은 class가 지정하는 함수
            self.content = content

        def read(self):                          # 직접 지정하는 함수
            self.view_count = self.view_count + 1 # 글 1번 읽을때마다 조회수 늘어남

# - 프로그래밍 언어는 영어랑 비슷
# - __init__, self는 하나의 약속으로 보면 됨.
# - self : class안에 있는 변수들에 접근하겠다는 약속
#   * 외부에서 지정하는 함수는 self를 쓸 필요가 없음
#   * class안에서 쓰는 함수. class안에서 만든 함수라는 것을 알려줘야 함 --> self로
#   * class안의 함수의 경우(def..), class의 변수에 접근하기 위해 self를 붙여줘야 함

# <class 실행>
# TypeError: __init__() missing 2 required positional arguments: 'title' and 'content'
# - __init__이 없을 때는 에러가 안 났음
# - __init__을 썼을 때 title, content를 반드시 채워줘야 클래스 활성화 시킬 수 있음
# --> title, content 채우기
article1 = Article("개발","개발은 쉬워요") # 위에서 12줄로 쓴 내용을
article2 = Article("코칭","코칭은 쉬워요") # 3줄로 줄인 효과
article3 = Article("창업","창업은 쉬워요")

# class의 장점
# - 위의 12줄처럼 많은 내용 class로 지정해줌으로써 (class Article: ...)
# - 이후의 코드가 편해짐 (바로 위 3줄 코드)
# ex) status라는 변수를 추가 시
#    위 12줄 코드에 일일히 status 추가 해야함
#    but, class 함수 밑에 status 한 번만 적어도 됨

# 조회 수 class 실행
# print(article1.view_count)
#
# article1.read()  # 글 1번 읽었을 때
# print(article1.view_count)

# 만일 class 안에 함수를 만들어놓지 않았다면
# article1.view_count1 = article.view_count1 + 1
# 이 코드를 모든 article의 조회수를 늘릴 때마다 써줘야 함
# but class 내부에 read()함수를 지정하여 불필요한 코드 작업 x
# read함수를 1번 호출하면 작업이 다 이루어짐
# article2.read()도 똑같이 진행


##### Article class inheritance (상속)
class BrunchArticle(Article): # Article이라는 class의 내용을 다 가지고 옴.
    source = "브런치"

brunch_article = BrunchArticle("개발","개발은 쉬워요")
# - BrunchArticle class 활성화
# - __init__에 title과 content를 넣어줘야 함
print(brunch_article.title)
# - BrunchArticle 안에서는 아무런 내용도 구현하지 않았다.
# - but BrunchArticle의 부모 class인 Article에서 title을 가지고 있음.

print(brunch_article.source)
# -새로 추가한 변수 source 확인

print(brunch_article.view_count)
brunch_article.read() # 1번 조회
print(brunch_article.view_count)
# - 변수 뿐 아니라 부모클래스가 가진 함수도 가지고 옴
# - 비교 위해 view_count 한 번 더 찍기



## 부모 클래스에서 가진 함수를 자식 클래스에서 덮어쓸 수 있다.
# --> override? 같은 함수를 다른 내용으로 썼다는 뜻
# 자식 class에서 해당하는 함수를 새로 정의할 경우,
# 자식 class에서는 새로 정의한 함수를 사용한다.
# <ex...>
# class BrunchArticle(Article): # Article이라는 class의 내용을 다 가지고 옴.
#     source = "브런치"
#
#     def read(self):
#         self.view_count = self.view_count + 2
