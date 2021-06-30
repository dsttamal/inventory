from django.urls import path
from inventory import views

urlpatterns = [
    path('clients', views.client, name='client'),
    path('suppliers', views.supplier, name='supplier'),
    path('', views.index, name='index'),
]