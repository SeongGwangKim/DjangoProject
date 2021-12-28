from django.urls import path

from . import views  # add
from django.conf import settings # add
from django.conf.urls.static import static # add

app_name = 'imageprocessingapp'


urlpatterns = [
    # TemplateView : 장고에서 제공하는 기본 뷰로 템플릿만 지정해주면 알아서 만들어 준다.
    # url(r'^$', views.first_view, name='first_view'),
    # url(r'^uimage/$', views.uimage, name='uimage'),
    path('first_view/', views.first_view, name='first_view'),
    path('uimage/', views.uimage, name='uimage'),
    path('dface/', views.dface, name='dface'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)