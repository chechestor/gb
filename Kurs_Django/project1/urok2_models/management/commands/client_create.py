import datetime
from django.core.management.base import BaseCommand
from urok2_models.models import Client

class Command(BaseCommand):
    help = "Create client"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client Name')
        parser.add_argument('email', type=str, help='Email')
        parser.add_argument('phone', type=str, help='Phone number')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, name, email="", phone="", address="", *args, **kwargs):
        client = Client(
            name = name,
            email = email,
            phone = phone,
            address = address,
            reg_date = datetime.datetime.now())
        client.save()
        self.stdout.write(f'{client}')

