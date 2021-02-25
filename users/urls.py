from django.urls import path
from django.conf.urls import url

from users import views


urlpatterns = [
    #path('register/', views.RegistrationView.as_view(), name="register"),
    #path('username-validtion/', views.UsenameValidationView.as_view(), name="username-validation"),
    path('', views.home, name='home'),
    path('authenticate/login/', views.login_view, name='login'),
    path('authenticate/signup/login/', views.login_view, name="signin"),
    #url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('authenticate/signup/', views.signup, name='signup'),
    path('authenticate/', views.authenticate, name="authenticate"),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
]
