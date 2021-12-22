from django.core.management.base import BaseCommand, CommandError

from blog.models import Category
from blog.utils.factory import generate_posts


class Command(BaseCommand):

    def handle(self, *args, **options):
        ctg_poems, ctg_travel, ctg_stories = Category.objects.all().order_by('id')

        generate_posts(ctg_poems)
        generate_posts(ctg_travel)
        generate_posts(ctg_stories)

        self.stdout.write(self.style.SUCCESS('Posts were successfully created.'))
