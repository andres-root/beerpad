# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def index(request):
    return HttpResponse("It works!")


def payment(request):
    id = request.GET.get('id', '')
    response = {'id': id}
    return JsonResponse(response)
