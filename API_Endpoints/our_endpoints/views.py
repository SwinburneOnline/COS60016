from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
import datetime

from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["GET"],)
def get_current_server_time(request):

    return HttpResponse(datetime.datetime.now())

@csrf_exempt

@require_http_methods(["POST"],)
def upload_file(request):
    file = request.FILES['text']
    with open(file.name, 'wb') as dst:
        for chunk in file.chunks():
            dst.write(chunk)
        return HttpResponse(status=200)

from our_endpoints.views import get_current_server_time, upload_file

# urlpatterns will be used to define paths to our views
urlpatterns = [
    path('server_time/', get_current_server_time),
    path('upload_file/', upload_file),
]

app_name = 'our_endpoints'

from uptime import uptime

@require_http_methods(["HEAD"])
def check_connection(request):
    response = HttpResponse(status=200)
    response[ 'Server_Status' ] = 'Up'
    response[ 'Up_time' ] = uptime()
    return response

from our_endpoints.views import get_current_server_time, upload_file, check_connection

urlpatterns = [
    path('server_time/', get_current_server_time),
    path('upload_file/', upload_file),
    path('status2/', check_connection),
]
app_name = 'our_endpoints'


import json
@csrf_exempt
@require_http_methods(["PUT"])
def save_json_to_file(request):
    json.loads
    data = json.loads(request.body)
    json_object = json.dumps(data, indent=4)

    with open("JSON_Data.json", "a") as f:
        f.write(json_object)

        return HttpResponse(status=200)


import os
@csrf_exempt@require_http_methods(["DELETE"])
def delete_file(request):
    data = json.loads(request.body)
    try:
        os.remove('My_Files/' + data['file_name'])
        return HttpResponse(status=200)
    except OSError:
        return HttpResponse(status=500)


from our_endpoints.views import get_current_server_time, upload_file, check_connection, save_json_to_file, delete_file

urlpatterns = [
    path('server_time/', get_current_server_time),
    path('upload_file/', upload_file),
    path('status2/', check_connection),
    path('save_json_to_file/', save_json_to_file),
    path('delete_file/', delete_file)
]

app_name = 'our_endpoints'



@csrf_exempt
@require_http_methods(["PATCH"])
def update_file(request):
    data = json.loads(request.body)
    with open('records.txt', 'a') as f:

        f.write(data[ 'updates' ])
        return HttpResponse(status=200)


from our_endpoints.views import get_current_server_time, upload_file, check_connection, save_json_to_file, delete_file, update_file

urlpatterns = [
    path('server_time/', get_current_server_time),
    path('upload_file/', upload_file),
    path('status2/', check_connection),
    path('save_json_to_file/', save_json_to_file),
    path('delete_file/', delete_file),
    path('update_file/', update_file)
]

app_name = 'our_endpoints'

