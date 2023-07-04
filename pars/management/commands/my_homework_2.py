# from django.core.management.base import BaseCommand
# from pars.models import Pars
#
#
# class Command(BaseCommand):
#     help = 'Перенос данных в модель'
#
#     def handle(self, *args, **options):
#         list_log = []
#         with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#             for line in f:
#                 total = line.split(' ')
#                 a_tuple = (total[0], total[5].replace('"', ''), total[6])
#                 list_log.append(a_tuple)
#                 # print(a_tuple)
#
#         for lines in list_log:
#             ip_address = Pars(
#                 ip=lines[0],
#                 type_request=lines[1],
#                 request=lines[2],
#             )
#             ip_address.save()
#         self.stdout.write(self.style.SUCCESS('Данные успешно перенесены'))

from django.core.management.base import BaseCommand
from pars.models import Pars


class Command(BaseCommand):
    help = 'Пернос данных в модель'

    def handle(self, *args, **options):
        list_log = []
        with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
            for line in f:
                total = line.split(' ')
                a_tuple = (total[0], total[5].replace('"', ''), total[6])
                list_log.append(a_tuple)

        for lines in list_log:
            ip_address = Pars(
                ip=lines[0],
                type_request=lines[1],
                request=lines[2],
            )
            ip_address.save()
        self.stdout.write(self.style.SUCCESS('Данные успешно перенесены'))
