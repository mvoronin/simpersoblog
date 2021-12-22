from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['pk']

    def __str__(self):
        return 'Category #%(pk)s "%(name)s"' % {'pk': self.pk, 'name': self.name}

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = 'DRF', 'Draft'
        PUBLISHED = 'PBL', 'Published'

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=StatusChoices.choices, default=StatusChoices.DRAFT)

    class Meta:
        ordering = ['-published', '-updated']

    def __str__(self):
        return 'Post #%(pk)s "%(title)s"' % {'pk': self.pk, 'title': self.title[:16]}

    def get_absolute_url(self):
        return reverse('post', kwargs={'ctg_slug': self.category.slug, 'pk': self.pk})

    def publish(self):
        self.status = self.StatusChoices.PUBLISHED
