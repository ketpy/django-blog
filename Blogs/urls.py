from django.urls import path
from . import views

urlpatterns = [
	path('', views.Home, name = "home" ),
	path('new/', views.NewPost, name = "new_blog" ),
	path('post/<int:id>/<slug:blog_slug>/', views.PerPost, name = "per_post"),
	path('update/<int:id>/<slug:blog_slug>/', views.EditPost, name = "edit_post"),
	path('delete/<int:id>/<slug:blog_slug>/', views.DeletePost, name = "delete_post"),
]