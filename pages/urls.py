# pages/url.py
from django.urls import path

from .views import HomePageView, AboutPageView #points to portfolio_kenny>pages>view.py

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
