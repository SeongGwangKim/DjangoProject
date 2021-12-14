from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):

    # request받은 메소드가 POST일 경우에
    if request.method == "POST":
        # POST로 되어 있고 hello_world_input이라는 이름을 가진 것에서 내용을 가져와서 temp에 담는다.
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        # db.sqlite3라는 db에 저장이 된다.
        new_hello_world.save()

        # return HttpResponse('Hello World!')
        #  context={'text': 'POST METHOD!!'} : text라는 이름을 가지고 있고 내용은 POST METHOD!!로 설정.
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world })
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!'})
