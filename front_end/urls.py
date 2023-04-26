from django.urls import path, include
from front_end.views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    
]