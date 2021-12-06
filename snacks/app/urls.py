from django.urls import path
from django.urls.resolvers import URLPattern
# from .views


URLPatterns = [
    path('about-us/', AboutUsView.as_view(), name = 'home'),
]