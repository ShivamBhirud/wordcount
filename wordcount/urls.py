from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name='home'),
    path("count", views.count, name='countvar'),
    path("about", views.about, name='about')
]
