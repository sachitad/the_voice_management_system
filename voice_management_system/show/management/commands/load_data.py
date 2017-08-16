from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

from show.factories import create_data
User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        if User.objects.all().count() > 1:
            self.stdout.write(self.style.ERROR(_('Data already loaded!')))
        else:
            create_data()
            self.stdout.write(
                self.style.SUCCESS(_('Successfully created dummy data')))
