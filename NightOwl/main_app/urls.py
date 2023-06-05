from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('owls/<int:owl_id>/add_photo/', views.add_photo, name='add_photo'),
]