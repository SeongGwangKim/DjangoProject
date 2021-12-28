from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/first_view.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

# MultipleObjectMixin는 여러가지 object를 다룰 수 있게 만들어줌
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/uimage.html'

    paginate_by = 25

    # 템플릿 창에서 object_list라는 것을 사용해서 필터링한 게시글들을 사용할 수 있게 만듦
    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user

        # 로그인이 되어 있으면 True를 반환
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        # 로그인이 안되어 있을 때
        else:
            subscription = None

        object_list = Article.objects.filter(project = self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list, subscription=subscription, **kwargs)


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25