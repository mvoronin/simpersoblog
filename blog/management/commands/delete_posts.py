from django.core.management.base import BaseCommand, CommandError

from blog.utils.factory import delete_posts


class Command(BaseCommand):

    def handle(self, *args, **options):
        ctg_poems = None
        delete_posts(ctg_poems)

        self.stdout.write(self.style.SUCCESS('Posts were successfully deleted.'))
