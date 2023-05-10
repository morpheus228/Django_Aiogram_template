from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='Telegram ID')
    username = models.CharField(max_length=255, null=True, verbose_name='Telegram username')
    first_name = models.CharField(max_length=255, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=255, null=True, verbose_name='Фамилия')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.first_name} {self.last_name} (@{self.username} id{self.id}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['created_at']
