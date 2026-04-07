from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('job-filter', views.Job_Filter_view, name='job-filter'),
    path('job-post', views.Job_Post_View, name='job-post'),
    path('job-detail/<int:pk>', views.Job_Detail_View, name='job-detail'),
    path('job-apply/<int:pk>', views.Job_Apply_view, name='job-apply'),
    path('notification', views.Notification_Views, name='notification'),
    path('applited-jobs', views.Applied_Job_View, name='applited-jobs'),
    path('job-applicants/<int:pk>/', views.Job_Applicants_View, name='job-applicants'),
]