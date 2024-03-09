from django.urls import path
from scp_api_app.views import currency_converter, index

urlpatterns = [
    path('', index, name='index'),
    path('convert/', currency_converter, name='convert'),
]