from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

# 경로 관련 에러는 urls를 확인한다!
# url로 불러오려면 app_name을 통해서 불러온다.
# app_name은 namespace와 관련이 있다.
app_name = 'articleapp'


urlpatterns = [
    # TemplateView : 장고에서 제공하는 기본 뷰로 템플릿만 지정해주면 알아서 만들어 준다.
    path('list/', ArticleListView.as_view(template_name='articleapp/list.html'), name='list'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete'),
]