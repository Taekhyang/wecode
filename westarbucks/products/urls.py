from django.contrib import admin
from django.urls import path, include

from .views import CategoryView, DrinkView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('/drink', DrinkView.as_view())
]
