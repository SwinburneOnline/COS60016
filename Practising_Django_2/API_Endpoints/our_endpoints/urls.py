from django.urls import path
from our_endpoints.views import get_current_server_time, upload_file, check_connection, save_json_to_file, delete_file, update_file




# urlpatterns will be used to define paths to our views

urlpatterns = [
    path('server_time/', get_current_server_time),
    path('upload_file/', upload_file),
    path('status/', check_connection),
    path('save_json_to_file/', save_json_to_file),
    path('delete_file/', delete_file),
    path('update_file/', update_file)
    path('check_connection/', check_connection)
]

app_name = 'our_endpoints'
