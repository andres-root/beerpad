# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Bar, Client


def index(request):
    return HttpResponse("It works!")


def payment(request):
    total = 0
    phone = request.GET.get('phone', '')
    barname = request.GET.get('bar', '')
    table = request.GET.get('table', '')
    beer_amount = request.GET.get('beer', '')
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
        return JsonResponse(response)
    except:
        error_message = 'An error has ocurred. Please try again.'
        response = {
            'status': 'error',
            'message': error_message
        }
        return JsonResponse(response)
