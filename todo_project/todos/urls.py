from django.urls import path

from .views import ListView, DetailView

urlpatterns = [
    path('<int:pk>', DetailView.as_view()),
    path('', ListView.as_view())
]
