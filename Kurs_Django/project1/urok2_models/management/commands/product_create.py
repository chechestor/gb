import datetime
from django.core.management.base import BaseCommand
from urok2_models.models import Product

class Command(BaseCommand):
    help = "Create product"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client Name')
        parser.add_argument('price', type=float, help='Price')
        parser.add_argument('quantity', type=str, help='Quadtity of a production on a store.')
        parser.add_argument('description', type=str, help='Product description')


    def handle(self, name, price="", quantity="", description="", *args, **kwargs):
        client = Product(
            name = name,
            price = price,
            quantity = quantity,
            description = description,
            reg_date = datetime.datetime.now())
        client.save()
        self.stdout.write(f'{client}')

