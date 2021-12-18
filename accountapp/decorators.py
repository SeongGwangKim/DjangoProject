from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        # << 본인인지 확인하는 작업 >>
        # User를 가져오고 objects를 get하고 pk가 pk인 값을 가지고 있는 유저 오브젝트가 user
        user = User.objects.get(pk=kwargs['pk'])

        # pk가 보낸 user가 요청을 보낸 user가 맞는지 확인인
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated