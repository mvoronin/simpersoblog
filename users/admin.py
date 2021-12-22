from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models import Contacts

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_filter = ('email', )
