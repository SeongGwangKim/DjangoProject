from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def hello_world(request):

    # request받은 메소드가 POST일 경우에
    if request.method == "POST":
        # return HttpResponse('Hello World!')
        #  context={'text': 'POST METHOD!!'} : text라는 이름을 가지고 있고 내용은 POST METHOD!!로 설정.
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!'})
