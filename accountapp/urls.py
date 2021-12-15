from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"


urlpatterns = [
    # 함수형 view는 함수형 view의 이름(hello_world)을 써주면 된다.
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    # 회원가입을 할 경로를 지정
    # class형 view는 class명.as_view()를 써줘야 한다.
    path('create/', AccountCreateView.as_view(), name='create')
]