from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path("clothes", views.clothes, name="clothes"),
    path("about", views.about, name="about"),
    path("form", views.form, name="form")
]
