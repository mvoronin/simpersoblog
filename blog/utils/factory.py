import random
from typing import List, Optional

import factory

from ..models import Category, Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Post'  # Equivalent to ``model = myapp.models.User``

    title = factory.Faker('sentence', nb_words=random.randrange(3, 12))
    description = factory.Faker('paragraph', nb_sentences=5, variable_nb_sentences=True)
    body = factory.Faker('paragraph', nb_sentences=20, variable_nb_sentences=True)


def generate_categories() -> [Category, Category, Category]:
    ctg_poems = Category.objects.create(name='Poems', slug='poems')
    ctg_travel = Category.objects.create(name='Travel', slug='travel')
    ctg_stories = Category.objects.create(name='Story', slug='stories')

    return ctg_poems, ctg_travel, ctg_stories


def generate_posts(ctg: Category, num: Optional[int] = None) -> List[Post]:
    if num is None:
        num = random.randrange(6, 20)

    posts = []

    for i in range(num):
        posts += [generate_post(ctg)]

    return posts


def generate_post(ctg: Category) -> Post:
    return PostFactory(category=ctg)


def delete_posts(ctg: Category) -> None:
    posts = Post.objects.all()
    if ctg:
        posts = posts.filter(category=ctg)
    posts.delete()
