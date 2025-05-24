from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class About_us(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name="Изображение")
 
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title