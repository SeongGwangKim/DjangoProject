from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        # 타이틀, 이미지, 컨텐트를 입력 받아서 보낼 수 있도록 설정
        fields = ['image', 'title', 'description']

        # migration 작업 : python manage.py makemigrations
        # python manage.py migrate하면 db에 반영

