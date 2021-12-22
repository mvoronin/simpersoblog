from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return '%(username)s [%(email)s] #%(id)s' % {'email': self.email, 'username': self.username, 'id': self.id}


class Contacts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return 'Contacts #%(pk)s for User #%(user_id)s' % {'pk': self.pk, 'user_id': self.user_id}
