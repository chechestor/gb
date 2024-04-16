from django.core.management.base import BaseCommand
from urok2_models.models import Order

class Command(BaseCommand):
    help = "List orders from DB"

    def handle(self, *args, **kwargs):
        order = Order.objects.all()
        for _o in order:
            self.stdout.write(f'{_o}\n')
            for p in _o.products.all():
                self.stdout.write(f'  :{p}\n')


