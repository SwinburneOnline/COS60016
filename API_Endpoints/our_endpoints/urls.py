from django.urls import path

from our_endpoints.views import get_current_server_time

urlpatterns = [
  path('server_time/', get_current_server_time),
]
from django.urls import path
from django.urls import path

from django.urls import path

from our_endpoints.views import get_current_server_time, upload_file, check_connection, save_json_to_file

urlpatterns = [
    path('server_time/', get_current_server_time),
    path('upload_file/', upload_file),
    path('status2/', check_connection),
    path('save_json_to_file/', save_json_to_file),
]

app_name = 'our_endpoints'

from django.urls import path

from django.urls import path

