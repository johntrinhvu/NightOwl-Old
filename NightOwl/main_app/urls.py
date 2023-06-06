from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.events_index, name='index'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('events/<int:event_id>/add_photo/', views.add_photo, name='add_photo'),
]