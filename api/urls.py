from home.views import *
from django.urls import path,include

urlpatterns = [
    path('animals/',AnimalView.as_view())
]