from django.urls import path,include
from . import views

app_name = 'endpoint'
urlpatterns = [
    path('get_info/', views.get_info, name='get_info'),
]
