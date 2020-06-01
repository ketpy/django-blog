from django.urls import path
from . import views

urlpatterns = [
	path('signup/', views.signup, name = "signup" ),
	path('profile/<slug:username>/', views.PublicProfile, name = "PublicProfile" ),
	path('update/profile/', views.profile, name = "profile"),
	path('logout/', views.logout_user, name = "logout_user")
]