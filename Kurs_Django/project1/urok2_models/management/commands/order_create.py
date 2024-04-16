import datetime
from django.core.management.base import BaseCommand
from urok2_models.models import Order, Client, Product

class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=str, help='Client Name')
        #parser.add_argument('products_ids', type=list[int], help='Products list')
        parser.add_argument('products_ids', nargs='*', help='Products ids list')


    def handle(self, client_id, products_ids, **kwargs):

        client = Client.objects.filter(pk=client_id).first()
        products__ = Product.objects.filter(pk__in=products_ids)

        self.stdout.write("=============================")
        self.stdout.write(f"{products_ids=}")
        for p in products__:
            self.stdout.write(f"{p=}")
        self.stdout.write("=============================")

        total_price = 1
        total_price = sum(product.price for product in products__)

        order = Order(
            client = client,
            total_price = total_price,
            reg_date = datetime.datetime.now(),
            #products = products__
        )

        order.save()
        for p in products__:
            order.products.add(p)
        order.save()

        self.stdout.write(f'{order}')

