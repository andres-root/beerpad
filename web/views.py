# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("It works!")


def payment(request):
    phone = request.GET.get('phone', '')
    bar = request.GET.get('bar', '')
    table = request.GET.get('table', '')
    beer_amount = request.GET.get('beer', '')
    split_fare = request.GET.get('split', '')

    if split_fare != '':
        split_mates = split_fare.split(',')
    response = {'status': 'ok'}
    return JsonResponse(response)
