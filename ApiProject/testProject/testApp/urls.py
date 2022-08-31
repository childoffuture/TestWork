from django.urls import path, include
from .views import *

urlpatterns = [
    path('visited_links', getLink),
    path('visited_domains', postLink),
]
