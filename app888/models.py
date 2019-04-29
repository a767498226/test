from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=16, unique=True, null=False)
    password = models.CharField(verbose_name="密码", max_length=16, null=False)
    nickname = models.CharField(verbose_name="昵称", max_length=32, null=True)




