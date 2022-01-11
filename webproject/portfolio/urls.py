from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('projects/', views.posts, name='projects'),
    path('post/<str:pk>/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    
    #CRUD
    
    path('createPost/', views.createpost, name='createPost'),
    
    #email
    path('email/', views.sendEmail, name='sendmail')
]
