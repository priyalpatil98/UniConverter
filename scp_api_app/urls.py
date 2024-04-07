from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('convert/', views.convert, name='convert'),
    path('crypto/', views.crypto_rates, name='crypto'),
    # path('stocks/', views.stocks_rates, name='stocks'),

]