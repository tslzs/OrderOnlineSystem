from django.urls import path

from . import views

app_name = "MerchantSystem"

urlpatterns = [
    path('', views.base_view,name = 'base'),
    path('getCash/',views.getCash_view),
    path('dealItem/',views.dealItem_view)
]

