from django.urls import path
from django.contrib.auth.decorators import login_required
from pages import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('profile', views.ProfileView, name='profile'),
    path('add_users', views.BulkAddUsers, name='add_users'),
    path('change_password',
         login_required(views.CustomPasswordChangeView.as_view()),
         name='change_password'),
]
