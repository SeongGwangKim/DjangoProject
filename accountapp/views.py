from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

has_ownership = [login_required, account_ownership_required]

# 함수형 view
@login_required
def hello_world(request):
# @login_required가 들어감으로써 필요가 없어짐
# user.is_authenticated : 유저가 로그인했는지
# if request.user.is_authenticated:
#     # request받은 메소드가 POST일 경우에
    if request.method == "POST":
        # POST로 되어 있고 hello_world_input이라는 이름을 가진 것에서 내용을 가져와서 temp에 담는다.
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        # db.sqlite3라는 db에 저장이 된다.
        new_hello_world.save()

        # HelloWorld의 모든 데이터를 긁어 올 수 있다.
        hello_world_list = HelloWorld.objects.all()

        # return HttpResponse('Hello World!')
        #  context={'text': 'POST METHOD!!'} : text라는 이름을 가지고 있고 내용은 POST METHOD!!로 설정.
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        # POST 메소드가 들어왔을 때 그것을 유지하는 것이 아니라 POST 메소드가 실행될 때만 불러오게 만듦
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        # HelloWorld의 모든 데이터를 긁어 올 수 있다.
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
# @login_required가 들어감으로써 필요가 없어짐
# else:
#     return HttpResponseRedirect(reverse('accountapp:login'))

# class형 view
class AccountCreateView(CreateView):
    # 해당 패키지의 정보를 보고 싶으면 그 곳에 Ctrl + b를 눌러서 확인
    model = User
    # 만들 때 사용할 폼이 필요하다.
    form_class = UserCreationForm
    # 이 계정을 만들기에 성공을 했다면 어느 경로에 연결을 할 것인가 연결해줄 곳을 연결
    # reverse_lazy는 class형 view에서 사용, reverse는 함수형 view에서 사용한다.
    success_url = reverse_lazy('accountapp:hello_world')
    # 회원가입을 할 때 볼 html 설정
    template_name = 'accountapp/create.html'


# 어떤 모델을 쓸지 그 모델 안의 정보를 어떻게 시각화할지만 신경써주면 됨
class AccountDetailView(DetailView):
    model = User
    # 템플릿에서 사용하는 유저 객체 이름을 다르게 설정하기 -> 다른 사람이 봐도 볼 수 있게하기
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

# @method_decorator : 일반 function에 사용하는 데코레이터를 메소드에 사용할 수 있도록 변환해주는 데코레이터
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
# 메소드 데코레이터를 배열에 넣고 주면 get과 post에 각각 밑에와 같이 주는 것과 똑같다.
# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')
class AccountUpdateView(UpdateView):
    # 해당 패키지의 정보를 보고 싶으면 그 곳에 Ctrl + b를 눌러서 확인
    model = User
    # 템플릿에서 사용하는 유저 객체 이름을 다르게 설정하기 -> 다른 사람이 봐도 볼 수 있게하기
    context_object_name = 'target_user'
    # 만들 때 사용할 폼이 필요하다.
    form_class = AccountUpdateForm
    # 이 계정을 만들기에 성공을 했다면 어느 경로에 연결을 할 것인가 연결해줄 곳을 연결
    # reverse_lazy는 class형 view에서 사용, reverse는 함수형 view에서 사용한다.
    success_url = reverse_lazy('accountapp:hello_world')
    # 회원가입을 할 때 볼 html 설정
    template_name = 'accountapp/update.html'

    # @method_decorator가 들어감으로써 필요 없어짐.
    # # self는 AccountUpdateView를 의미한다.
    # # self.get_object() == self.request.user : pk에 해당하는 object가 현재 request를 보내는 user와 같은지 확인
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         # 금지되어 있는 곳으로 접근을 한 것을 보여준다.
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         # 금지되어 있는 곳으로 접근을 한 것을 보여준다.
    #         return HttpResponseForbidden()


# @method_decorator : 일반 function에 사용하는 데코레이터를 메소드에 사용할 수 있도록 변환해주는 데코레이터
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    # 템플릿에서 사용하는 유저 객체 이름을 다르게 설정하기 -> 다른 사람이 봐도 볼 수 있게하기
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    # @method_decorator가 들어감으로써 필요 없어짐.
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         # 금지되어 있는 곳으로 접근을 한 것을 보여준다.
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         # 금지되어 있는 곳으로 접근을 한 것을 보여준다.
    #         return HttpResponseForbidden()
