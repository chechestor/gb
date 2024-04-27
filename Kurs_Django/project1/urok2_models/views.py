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

from .models import Order, Client, Product

from .forms import ImageAddForm
from django.core.files.storage import FileSystemStorage

from django.conf import settings
from django.conf.urls.static import static



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

class Template_ViewAllProducts(TemplateView):
    template_name = "urok2_models/products.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        content_products = []

        for prod in products:
            # MEDIA_URL = '/media/'
            # MEDIA_ROOT = BASE_DIR / 'media'


            #url = FileSystemStorage().url(prod.picture)
            #url = FileSystemStorage().base_url + prod.picture
            url = prod.picture
            #url = MEDIA_URL + prod.image


            logging.info(f'===================== {url=}')
            logging.info(f'                      {settings.MEDIA_URL=}')
            logging.info(f'                      {settings.STATIC_URL=}')


            content_products.append({'id': f'{prod.pk}',
                                     'text': f'{prod}',
                                     'image_url': f'{url}' })
        context['products'] = content_products
        return context

class Template_ProductImageSet(TemplateView):
    template_name = "urok2_models/upload_image.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        logging.info(f'{self.request.method}')

        form = ImageAddForm()

        context['form'] = form

        if 'error_message' in kwargs:
            logging.info(f'ERROR MESSAGE = {kwargs}')
            context['error_message'] = kwargs['error_message']

        return context

    def post(self, request, *args, **kwargs):

        form = ImageAddForm(self.request.POST, self.request.FILES)
        error_message = None
        ok_message = None
        if form.is_valid():
            logging.info("+++++++++++++ ok ++++++++++++++++++++++++++++++++")
            image = form.cleaned_data['image']

            fs = FileSystemStorage()
            filename = str(hash(datetime.datetime.now().isoformat())) + "_" + image.name
            fileobj = fs.save(filename, image)

            logging.info(f'\n\n{fileobj}\n\n')

            prod1 = Product.objects.filter(pk = form.cleaned_data['product_id']).first()
            logging.info(f'{prod1.picture}')
            #prod1.image = filename
            prod1.picture = filename
            prod1.save()

            ok_message = "картинка успешно сохранена"

        else:
            error_message = "Не удалось прикрепить картинку. Проверьте id продукта."

        return self.render_to_response(self.get_context_data(form=form, error_message=error_message, ok_message=ok_message))

