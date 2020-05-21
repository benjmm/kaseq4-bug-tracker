from django.urls import path
from appbug import views

urlpatterns = [
    path('', views.index_v, name='index'),
    path('error/', views.error_v, name='error'),
    # path('register/', views.register_v, name='register'),
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_v, name='logout'),
    path('home/', views.home_v, name='home'),
]
