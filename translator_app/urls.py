from django.urls import path
from . import views

urlpatterns = [
    path('', views.translate_view, name = "translate"),
]