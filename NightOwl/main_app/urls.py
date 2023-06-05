from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    # path('owls/<int:owl_id>/add_photo/', views.add_photo, name='add_photo'),
]