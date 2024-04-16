from django.core.management.base import BaseCommand
from urok2_models.models import Product

class Command(BaseCommand):
    help = "List clients from DB"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for p in products:
            self.stdout.write(f'{p}\n')

