from django.urls import path
from appbug import views

urlpatterns = [
    path('', views.index_v, name='index'),
    path('error/', views.error_v, name='error'),
]
