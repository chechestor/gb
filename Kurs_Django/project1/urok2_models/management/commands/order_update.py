import datetime
from django.core.management.base import BaseCommand
from urok2_models.models import Order, Product

class Command(BaseCommand):
    help = "Change order."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Irder id for delete.')
        parser.add_argument('products_ids', nargs='*', help='Products ids list')

    def handle(self, order_id, products_ids, **kwargs):
        order = Order.objects.filter(pk=order_id).first()
        if not order:
            self.stdout.write(f'No such order.')

        products__ = Product.objects.filter(pk__in=products_ids)

        order.total_price = sum(product.price for product in products__)

        order.products.clear()
        for p in products__:
            order.products.add(p)
        order.save()

        self.stdout.write(f'{order}')

