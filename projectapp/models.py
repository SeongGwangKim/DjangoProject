from django.db import models

# Create your models here.
from django.views.generic import ListView


class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # f' { } ' : ' ' 앞에 f를 붙이면 { } 안에 직접 변수를 출력할 수 있다.
        return f'{self.pk} : {self.title}'



