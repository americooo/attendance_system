from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('report/', views.report, name='report'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='attendance/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_student/', views.add_student, name='add_student'),
    path('report/download/', views.download_csv, name='download_csv'),


]
