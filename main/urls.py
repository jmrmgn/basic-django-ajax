from django.urls import path, include

from . import views

app_name = "main"

urlpatterns = [
   path('', views.index, name="index"),
   path('insert/', views.insert_data, name='insert_data'),
   path('get_user/', views.get_data, name='get_data')
]