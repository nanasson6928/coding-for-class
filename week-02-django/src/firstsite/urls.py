"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

# blog 폴더 안에 있는 urls를 가져와서 'blog'라는 이름을 붙여라
# urlpatterns = [
#     url(r'^blog/', include('blog.urls')),
#     url(r'^admin/', admin.site.urls),
# ]
urlpatterns = [
    url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]

# blog의 url.py 보다 가장 중심이 됨
# 이 url로 주소를 입력했을 때 가장 먼저 검색을 한다.
