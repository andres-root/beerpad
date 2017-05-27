# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Bar, Client, Transaction


def index(request):
    return HttpResponse("It works!")


def payment(request):
    total = 0
    subtotal = 0
    phone = request.GET.get('phone', '')
    barname = request.GET.get('bar', '')
    table = request.GET.get('table', '')
    beer_amount = request.GET.get('beer', '')
    discounts = request.GET.get('discounts', '')
    split_fare = request.GET.get('split', '')

    try:
        bar = Bar.objects.get(username=barname)
        client = Bar.objects.get(phone=phone)
        if split_fare != '':
            split_mates = split_fare.split(',')
            total = (bar.beer_cost * beer_amount) / len(split_mates)
            client.balance = client.balance - total
            client.save()
        else:
            total = bar.beer_cost * beer_amount
            client.balance = client.balance - total
            client.save()

        response = {'status': 'ok'}
        transaction = Transaction(
            client=client,
            bar=bar,
            table=table,
            discounts=discounts,
            beer_amount=beer_amount,
            subtotal=total,
            total=total
        )
        transaction.save()
        return JsonResponse(response)
    except:
        error_message = 'An error has ocurred. Please try again.'
        response = {
            'status': 'error',
            'message': error_message
        }
        return JsonResponse(response)
