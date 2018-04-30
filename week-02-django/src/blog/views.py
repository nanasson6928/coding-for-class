# from django.http import HttpResponse
from django.shortcuts import render
# from random import randint
from .models import Article
# - views.py와 같은 폴더안의 models.py에서 Article을 불러들임

# Create your views here.



def index(request):
    # random_number = randint(1, 10)
    # return HttpResponse("Hello, world. {}".format(random_number))
    # return HttpResponse("Hello, world. You're at the blog index")
    # name = "wjddk"
    # return render(request, "index.html", { "name" : name})
    article_list = Article.objects.all()
    # Article.objects.create(
    #     title = "hello",
    #     contents = "this is test",
    #     view_count = 0
    # )
    ctx = {
        "article_list" : article_list
    }
    return render(request, "index.html", ctx)

# views.py
# : 한 파일의 복잡한 코드를 단순하게 하기위해 독자적으로 떨어져 나온 부분.

# def index(request):
#     return render(request, "index.html", {})

# <Template> : views.py와 연결되어 작동
# 0. 역할
# - html에서 코드를 단순하게 짜고도 views.py에서 다양하게 조립시킬 수 있게 한다.

# 1.
# - views.py에서  render함수를 호출시키면
#   index.html(템플릿)에 작성한 <div>hello world</div>가 화면에 나타남
# 2.
# - views.py에서 함수에 name = "wjddk"를 추가하고
#   index.html에서 <div>hello world, {{ name }}</div>을 추가하면
#   웹에 "hello world, wjddk"가 출력된다.
# 3. 정리하면,
# - Template은 그 자체로 형태를 유지한다.
# - views.py를 통해서 템플릿의 특정값을 바꿔서 출력할 수 있다.
#   a. index.html(템플릿)의 어떤 특정 값을 넘겨준다고 약속한다. ex. {{ name }}
#   b. views.py에는 바꿀 값만 찍어준다.  ex. name = "wjddk"
# - view 기능이 없다면 템플릿을 두 개 만들어야 하는 불편을 해결함

# <Admin>
# def index(request):
#     article_list = Article.objects.all()
#     ctx = {
#         "article_list" : article_list
#     }
#     return render(request, "index.html", ctx)

# 1. ctx = {} : 앞으로 넘겨줘야 할 내용이 많기 때문에 dictionary 추가
# 2. Article.objects.all() : Article클래스로 등록되어 있는 모든 obs를 모두 불러옴
# 3. article_list 변수에 2번 값 할당
# 4. index에서 Article의 모든 obs를 가져와 views.py에 넘겨주면 템플릿에서 쓸 수 있음.
# 5. index.html에서 파이썬과 비슷한 걸 쓸 수 있음
#     {% for article in article_list %} : article을 하나씩 꺼냄.
#     - article_list를 views.py의 "article_list = Article.objects.all()"에서
#     넘겨주고 있으므로 index.html에서 for문을 돌릴 수 있다.
#     - {% for in %} 구문은 {% endfor %}로 닫아줘야 한다.
# 6. {% for article in article_list %} 구문 하위에
#     {{ article.title }} 추가 : article의 title을 찍어줌
