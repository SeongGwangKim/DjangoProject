from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    # models.CharField가 반드시 있어야 한다면 null=False로 지정한다 True이면 없어도 되는 것
    text = models.CharField(max_length=255, null=False)



