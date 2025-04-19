from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('User-Register/', views.user_register, name='User-Register'),
    path('logout/', views.logout_view, name='logout'),

    path('Organization-Register/', views.organization_register, name='Organization-register'),
    
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),
]