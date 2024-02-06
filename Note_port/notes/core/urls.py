from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views 
from . forms import LoginForm 

app_name = 'core'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('signup/', views.signup, name= 'signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'templates/auth/login.html', authentication_form = LoginForm), name= 'login'),
    path('logout/', views.logout_user, name= 'logout'),
    path('profile/', views.profile, name= 'profile'),

]

