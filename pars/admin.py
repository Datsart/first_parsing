# from django.contrib import admin
# from .models import Pars
#
#
# # Register your models here.
#
#
# class ParsAdmin(admin.ModelAdmin):
#     list_display = ('ip', 'type_request', 'request')
#
#
# # Создали и зарегали шаблон, в скобках: моя модель и то как он будет видна в админке, именно по данной модели
# admin.site.register(Pars, ParsAdmin)


from django.contrib import admin
from .models import Pars


class ParsAdmin(admin.ModelAdmin):
    list_display = ('ip', 'type_request', 'request')


admin.site.register(Pars, ParsAdmin)
