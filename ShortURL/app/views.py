from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from .models import URLGenerator
from .models import URL


# Create your views here.

def createshorturl(request : HttpRequest):
    url_generator = URLGenerator()
    main_url = request.GET.get("url")
    domain = request.get_host()
    if len(URL.objects.filter(url_address=main_url)) == 0:
        URL.objects.create(url_address=main_url)
        url = URL.objects.get(url_address=main_url)
        idx = url.id
        key = url_generator.generate_unique_key(idx)
        url.short_url =  domain + "/" + key
        url.save()
    else:
        url = URL.objects.get(url_address=main_url)
        key = url.short_url
    json_object = {
        'main_url' : main_url,
        'short_url' : url.short_url,
    }
    return JsonResponse(json_object)
