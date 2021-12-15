from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld

# 함수형 view
def hello_world(request):

    # request받은 메소드가 POST일 경우에
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


