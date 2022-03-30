from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home')
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('a_Django_app.urls')),
    path('admin/', admin.site.urls),
]