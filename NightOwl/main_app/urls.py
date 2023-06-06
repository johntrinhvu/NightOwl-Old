from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('events/', views.events_index, name='index'),
    path('', views.home, name='home'),
    path('events/<int:event_id>/', views.events_detail, name='detail'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('login/', LoginView.as_view(template_name='nightowl/login.html'), name='login_view'),
    
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
    # path('events/<int:event_id>/add_photo/', views.add_photo, name='add_photo'),
    # path('owls/<int:owl_id>/add_photo/', views.add_photo, name='add_photo'),
]