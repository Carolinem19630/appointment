from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:appointments_id>", views.appointments, name="appointments"),
    path("<int:appointments_id>/attend", views.attend, name="attend")
]