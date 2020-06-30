from django.urls import path
from . import views

# url routes
urlpatterns = [
    path('', views.home, name="hello-home"),
    path('about/', views.about, name="hello-about"),
]