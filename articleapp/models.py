from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# db설정
class Article(models.Model):
    # User가 지워지면 그 사람이 게시한 글도 다 지워지게 설정.
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    # 이미지 업로드를 article로부터 null 불가능
    image = models.ImageField(upload_to='article/', null=False)
    # 언제 만들어졌는지 생성 시간 저장
    created_at = models.DateField(auto_now_add=True, null=True)