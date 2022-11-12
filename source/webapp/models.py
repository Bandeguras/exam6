from django.db import models

# Create your models here.
STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Book(models.Model):
    author = models.CharField(max_length=30, verbose_name="Название")
    email = models.EmailField(max_length=45, verbose_name="Почта")
    description = models.TextField(max_length=3000, verbose_name="Описание")
    completion_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата выполнения")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name="Статус")