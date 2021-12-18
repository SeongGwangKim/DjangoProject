from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    # OneToOneField : 프로파일과 유저 객체를 연결해준다.
    # User, on_delete=models.CASCADE는 User객체가 삭제되면 그와 연결되어 있는 프로파일 객체도 같이 사라진다.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 이미지 설정
    image = models.ImageField(upload_to='profile/', null=True)
    # 닉네임 설정
    nickname = models.CharField(max_length=20, unique=True, null=True)
    # 넣을 메세지 설정
    message = models.CharField(max_length=100, null=True)

    # 각각을 db와 연동하기 위하여 python manage.py makemigrations를 한 후에
    # python manag.py migrate