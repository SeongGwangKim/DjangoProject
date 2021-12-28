"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# 새로운 기능을 추가하기 위해서는 python manage.py starteapp 만들_앱이름
# 그 다음에 urlpatterns에 라우팅시켜준다.
# admin 계정 만들기 : python manage.py createsuperuser
from articleapp.views import ArticleListView

urlpatterns = [
    # 기본 화면 설정
    path('', ArticleListView.as_view(), name='home'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    path('imageprocessing/', include('imageprocessingapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)가 있어야지 이미지를 서버가 보낼 수 있게 된다.
