# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Bar, Client, Transactions


def index(request):
    return HttpResponse("Welcome to Flash Beer")


def info(request):
    phone = request.GET.get('phone', '')
    barname = request.GET.get('bar', '')
    bar = Bar.objects.get(username=barname)
    client = Client.objects.get(phone=phone)
    bar_info = {
        'name': bar.name,
        'username': bar.username,
        'phone': bar.phone,
        'beer_cost': bar.beer_cost
    }
    client_info = {
        'name': client.name,
        'phone': client.phone,
        'balance': client.balance
    }
    response = {
        'bar': bar_info,
        'client': client_info
    }
    return JsonResponse(response)


def payment(request):
    total = 0
    subtotal = 0
    beer_cost = 0
    phone = request.GET.get('phone', '')
    barname = request.GET.get('bar', '')
    table = request.GET.get('table', '')
    beer_amount = request.GET.get('beer', '')
    discounts = request.GET.get('discounts', False)
    split_fare = request.GET.get('split', False)
    # try:
    bar = Bar.objects.get(username=barname)
    client = Client.objects.get(phone=phone)

    if not discounts:
        beer_cost = float(bar.beer_cost) * float(beer_amount)
    else:
        new_price = float(bar.beer_cost) - (float(bar.beer_cost) * float(discounts))
        beer_cost = new_price * float(beer_amount)

    if not split_fare:
        total = beer_cost * float(beer_amount)
        client.balance = client.balance - total
        client.save()
    else:
        split_mates = split_fare.split(',')
        total = beer_cost / len(split_mates)
        client.balance = client.balance - total
        client.save()

    response = {'status': 'ok'}
    transaction = Transactions(
        client=client,
        bar=bar,
        table=table,
        discounts=discounts,
        beer_amount=float(beer_amount),
        subtotal=subtotal,
        total=total
    )
    transaction.save()
    return JsonResponse(response)
    # except:
    #     error_message = 'An error has ocurred. Please try again.'
    #     response = {
    #         'status': 'error',
    #         'message': error_message
    #     }
    #     return JsonResponse(response)
