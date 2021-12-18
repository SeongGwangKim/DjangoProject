from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # 'accountapp:detail'에는 pk값인 추가적인 값이 들어가야 한다.
    # success_url = reverse_lazy('accountapp:detail')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # forms.py에서 날라온 데이터가 form 안에 들어가 있다.
        temp_profile = form.save(commit=False)
        # temp_profile.user : temp_profile에 user라는 데이터에 요청하는 user로 정해주고 저장한다.
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        # self가 가리키는 것은 Profile이다. 따라서 Profile의 user의 pk를 넘겨주게 된다.
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        # self가 가리키는 것은 Profile이다. 따라서 Profile의 user의 pk를 넘겨주게 된다.
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

