from django.forms import ModelForm
from django import forms

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    # 이유를 모르겠으나 왼쪽 정렬이 되지 않음... 'class': 'editable text-left', => 둘 중 하나만 설정됨
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Article
        # 타이틀, 이미지, 컨텐트를 입력 받아서 보낼 수 있도록 설정
        fields = ['title', 'image', 'project', 'content']

        # migration 작업 : python manage.py makemigrations
        # python manage.py migrate하면 db에 반영
