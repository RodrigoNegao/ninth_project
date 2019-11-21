from django.urls import path, re_path
from . import views
from . import models

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('updateuser/', views.updateuser, name='updateuser'),
    #re_path(r'^(?P<slug>[\w-]+)/$', views.Profile, name='profile'),
]
