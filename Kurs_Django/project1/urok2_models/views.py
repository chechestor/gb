'''
Урок 3.
Задание

Продолжаем работать с товарами и заказами.

Создайте шаблон, который выводит список заказанных клиентом товаров из всех его заказов с сортировкой по времени:
— за последние 7 дней (неделю)
— за последние 30 дней (месяц)
— за последние 365 дней (год)

Товары в списке не должны повторятся.

'''
import logging
logging.basicConfig(level=logging.INFO)

import datetime

from django.views.generic import TemplateView
from django.http import HttpResponse

from .models import Order, Client

class Template_ViewLastOrders(TemplateView):
    template_name = "urok2_models/user_orders.html"

    def get_context_data(self, user_id=None, period=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['comment'] = "Комментарий: укажите в адресной строке id юзера и период. Пример: .../1/day/  "

        if user_id:
            context['user_id'] = user_id

            # определяемся с условиями выборки
            conditions_translate = {
                'year': {'comment':'Заказы клиента за последний год.', 'timedelta': 356},
                'month': {'comment':'Заказы клиента за последний месяц.', 'timedelta': 30},
                'day': {'comment':'Заказы клиента за прошедшие сутки.', 'timedelta': 1},
                'week': {'comment':'Заказы клиента за последнюю неделю.', 'timedelta': 7}
            }
            if not period in conditions_translate:
                period = 'day'
            context['comment'] = conditions_translate[period]['comment']
            # ранняя дата отсечки
            edge_date = datetime.datetime.now() - datetime.timedelta(days=conditions_translate[period]['timedelta'])

            # получаем, фильтруем, собираем продукты
            orders = Order.objects.filter(client_id=user_id, reg_date__gte=edge_date).order_by('-reg_date')
            products_pks=set()
            products_list_dated=[]
            for _o in orders:
                for _p in _o.products.all():
                    if not _p.pk in products_pks:
                        products_pks.add(_p.pk)
                        products_list_dated.append(
                            {'product':f"{_p}",
                             'sale_date': f"{_o.reg_date}",
                             'order_id': f"{_o.pk}",
                             })
            context['products'] = products_list_dated

        return context


