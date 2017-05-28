from django.db import models

# Create your models here.


class Client(models.Model):
    name = models.CharField(max_length=400)
    phone = models.CharField(max_length=200)
    balance = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bar(models.Model):
    name = models.CharField(max_length=400)
    username = models.CharField(max_length=400)
    phone = models.CharField(max_length=200)
    beer_cost = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Transactions(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    bar = models.ForeignKey(Bar, on_delete=models.CASCADE)
    table = models.CharField(max_length=200)
    discounts = models.FloatField()
    beer_amount = models.FloatField()
    subtotal = models.FloatField()
    total = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        name = '{0} at {1}'.format(self.client, self.bar)
        return name
