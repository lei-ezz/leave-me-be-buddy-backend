from django.urls import path
from . import views

urlpatterns = [
    # two required: route and view, and two optional: kwargs, and name
    path("", views.index, name="index"),
]