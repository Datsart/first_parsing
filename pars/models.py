# from django.db import models
#
#
# # Create your models here.
# class Pars(models.Model):
#     ip = models.CharField(max_length=100, verbose_name='IP - адрес')
#     type_request = models.CharField(max_length=20, verbose_name='Тип запроса')
#     request = models.CharField(max_length=200, verbose_name='Запрос')
#
#     class Meta:
#         verbose_name_plural = 'Логи'
#         verbose_name = 'Лог'
#         ordering = ['-type_request']
#
#     def __str__(self):
#         return self.ip

from django.db import models

class Pars(models.Model):
    ip = models.CharField(max_length=100, verbose_name='IP - адрес')
    type_request = models.CharField(max_length=20, verbose_name='Тип запроса')
    request = models.CharField(max_length=200, verbose_name='Запрос')

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
        ordering = ['-type_request']

    def __str__(self):
        return self.ip