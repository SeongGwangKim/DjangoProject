from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):


    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        # project_pk를 가지고 있는 Project를 찾고 없다면 404 리스폰스를 돌려준다.
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user

        # Model.objects.filter는 and 조건 따라서 user & project가 모두 맞는 것이 실행된다.
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5


    def get_queryset(self):
        # values_list 받아온 값들을 리스트화 시킨다.
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        # project__in는 sql에서 select ~ where project in ( )과 같다.
        article_list = Article.objects.filter(project__in=projects)
        return article_list
