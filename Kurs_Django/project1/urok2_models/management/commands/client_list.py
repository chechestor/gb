from django.core.management.base import BaseCommand
from urok2_models.models import Client

class Command(BaseCommand):
    help = "List clients from DB"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        for c in clients:
            self.stdout.write(f'{c}\n')

