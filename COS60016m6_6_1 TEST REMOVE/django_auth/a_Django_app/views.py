from django.shortcuts import render

# Create your views here.

def authenticate(token):

    if token == AUTH_TOKEN:

        return True

    else:

        return False
