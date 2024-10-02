from django.urls import path
from .import views

urlpatterns = [
    path('registation/', views.Registation.as_view(), name='users'),
    path('login/', views.Login.as_view(), name='login'),
    path('user/', views.Users.as_view(), name='logout'),
    path('number_of_user/', views.AllUsers.as_view(), name='number_of_user'),

]