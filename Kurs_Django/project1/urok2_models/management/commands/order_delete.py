import datetime
from django.core.management.base import BaseCommand
from urok2_models.models import Order

class Command(BaseCommand):
    help = "Delete order."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Irder id for delete.')

    def handle(self, order_id, **kwargs):
        order = Order.objects.filter(pk=order_id).first()
        if order is not None:
            order.delete()
        self.stdout.write(f'{order}')

