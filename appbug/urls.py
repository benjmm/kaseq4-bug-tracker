from django.urls import path
from appbug import views

urlpatterns = [
    path('', views.index_v, name='index'),
    path('error/', views.error_v, name='error'),
    # path('register/', views.register_v, name='register'),
    path('login/', views.login_v, name='login'),
    path('logout/', views.logout_v, name='logout'),
    path('home/', views.home_v, name='home'),
    path('bug/<int:id>/', views.bug_v, name='bug'),
    path('user/<int:id>/', views.user_v, name='user'),
    path('addbug/', views.addbug_v, name='addbug'),
    path('assigntome/<int:id>/', views.assigntome_v, name='assigntome'),
    path('markdone/<int:id>/', views.markdone_v, name='markdone'),
    path('markinvalid/<int:id>/', views.markinvalid_v, name='markinvalid'),
    path('editbug/<int:id>/', views.editbug_v, name='editbug'),
]
