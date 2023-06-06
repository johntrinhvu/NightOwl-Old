from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='nightowl/login.html'), name='login_view'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]