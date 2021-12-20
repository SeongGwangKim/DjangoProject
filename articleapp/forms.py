from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        # 타이틀, 이미지, 컨텐트를 입력 받아서 보낼 수 있도록 설정
        fields = ['title', 'image', 'project', 'content']

        # migration 작업 : python manage.py makemigrations
        # python manage.py migrate하면 db에 반영

