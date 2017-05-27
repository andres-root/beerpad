from django.contrib import admin
from .models import Client, Bar, Transactions

admin.site.register(Client)
admin.site.register(Bar)
admin.site.register(Transactions)
