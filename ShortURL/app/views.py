from django.http.response import HttpResponseNotFound, JsonResponse
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


def redirect_url(request : HttpRequest):
    try:
        generator = URLGenerator()
        key = request.get_full_path().replace('/', '')
        idx = generator.get_id(key)
        url = URL.objects.get(id=idx)
        response = redirect(url.url_address)
        return response
    except Exception:
        return HttpResponseNotFound()