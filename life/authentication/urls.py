from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('signup/', views.registration, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('', views.SuperTest, name='test'),

]