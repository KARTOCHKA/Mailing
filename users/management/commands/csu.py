from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='admin@sky.ru',
            first_name='Admin',
            last_name='Adminovich',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('485967Wsx')
        user.save()
