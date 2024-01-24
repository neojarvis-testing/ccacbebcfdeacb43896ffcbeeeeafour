# In Day1Q2/urls.py
from django.contrib import admin
from django.urls import include, path
from Q2.views import greet_user
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', greet_user, name='greet_user'),  # Handle the root URL
    path('greet_user/', include('Q2.urls')),
]
