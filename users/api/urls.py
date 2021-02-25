from django.urls import path, include
from users.api.views import RegisterAPI, LoginAPI, UserAPI

#	registration_view,
#	ObtainAuthTokenView,
#	account_properties_view,
#	update_account_view,
#	does_account_exist_view,
#	ChangePasswordView,
#	UserLoginAPIView
#)
#from rest_framework.authtoken.views import obtain_auth_token

app_name = 'users'

urlpatterns = [
	#path('check_if_account_exists/', does_account_exist_view, name="check_if_account_exists"),
	#path('change_password/', ChangePasswordView.as_view(), name="change_password"),
	path('user', UserAPI.as_view(), name="properties"),
#	path('update', ObtainAuthTokenView.as_view(), name="update"),
 	path('login', LoginAPI.as_view(), name="login"), 
	path('register', RegisterAPI.as_view(), name="register"),

]