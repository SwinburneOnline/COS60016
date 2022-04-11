from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View
import json

AUTH_TOKEN = "JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF"

def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False

class AddView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 + num02)


class SubView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        AddView

        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 - num02)


class DivView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):

            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        if num02 == 0.0:
            return HttpResponse("Cannot divide by 0")
        else:
            return HttpResponse(num01 / num02)



class MultiView(View):
    def get(self, request):
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])
        return HttpResponse(num01 * num02)

