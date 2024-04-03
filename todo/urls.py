from django.urls import path
from .import views
 


urlpatterns = [
  path('', views.index, name= 'index'),
  path('login', views.login, name= 'login' ),
  path('logout/', views.LogoutView, name= 'logout'),
  path('register', views.register, name = 'register' ),
  path('create', views.create, name = 'create'),
  path('delete/<str:name>/',views.DeleteTask, name='delete'),
  path('update/<str:name>/', views.Update, name='update'),
  # path('accounts/profile/', views.profile, name='profile'),
  
]


