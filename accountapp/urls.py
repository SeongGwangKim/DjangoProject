from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

# 페이지에 들어가도록 라우팅을 하는 곳
urlpatterns = [
    # 함수형 view는 함수형 view의 이름(hello_world)을 써주면 된다.

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    # 회원가입을 할 경로를 지정
    # class형 view는 class명.as_view()를 써줘야 한다.
    path('create/', AccountCreateView.as_view(), name='create'),

    # 특정 유저의 정보를 보는 곳, 그 계정의 id(primary key)가 필요하다.
    # detail/<int:pk> /뒤에 pk라는 이름의 int 정보를 받겠다.(몇 번 유저의 정보를 받을 건지)
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),

    path('update<int:pk>', AccountUpdateView.as_view(), name='update'),

    path('delete<int:pk>', AccountDeleteView.as_view(), name='delete'),

]