from django.conf.urls import url
from . import views
# 같은 폴더에 있는 views.py를 불러옴

urlpatterns = [
    url(r'^$', views.index, name='index'),
]              # views.py의 index를 찍어줌


# url.py -- blog 는 view를 가리키는 주소를 나타낸 파일.
