from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cryptonews/', views.cryptonews, name="cryptonews"),
    path('ethpairs/', views.ethpairs, name="ethpairs"),
    path('btcpairs/', views.btcpairs, name="btcpairs"),
    path('usdpairs/', views.usdpairs, name="usdpairs"),
    path('cryptolookup/', views.cryptolookup, name="cryptolookup"),
]
