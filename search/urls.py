from django.urls import re_path, path

from . import views

urlpatterns = [
    path('', views.auto_complete, name='auto_complete'),
    path('submit_search', views.search, name='submit_search'),
]