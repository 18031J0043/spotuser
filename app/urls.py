from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signin),
    url(r'^postsignin/', views.postsignin),
    url(r'^logout/',views.logout,name="log"),
    url(r'^signup/', views.signup,name="sign"),
    url(r'^postsignup/', views.postsignup, name="postsignup"),
    url(r'^create/', views.create, name='create'),
    url(r'^post_create/', views.post_create, name='post_create'),
    



]
