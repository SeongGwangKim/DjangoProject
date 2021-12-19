from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # TemplateView : 장고에서 제공하는 기본 뷰로 템플릿만 지정해주면 알아서 만들어 준다.
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')

]