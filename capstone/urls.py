from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('adminlogin/', views.adminlogin_page, name="adminlogin_page"),
    path('adminregister/', views.adminregister_page, name="adminregister_page"),
    path('about/', views.aboutPage, name="aboutPage"),
    path('profile/', views.profile_page, name="profile_page"),
    path('updateprofile/', views.updateProfile, name="updateProfile"),
    path('announcement/', views.announcement_page, name="announcement_page"),
    path('market/', views.market_page, name="market_page"),
    path('reports/', views.reports_page, name="reports_page"),
    path('logout/', views.log_out, name="log_out"),
] 