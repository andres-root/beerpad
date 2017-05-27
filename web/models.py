from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=400)
    phone = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bar(models.Model):
    name = models.CharField(max_length=400)
    phone = models.CharField(max_length=200)
    beer_cost = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    table = models.CharField(max_length=200)
    discounts = models.DecimalField(max_digits=6, decimal_places=2)
    beer_amount = models.FloatField()
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
