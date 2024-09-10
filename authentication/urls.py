from django.urls import path
from .import views

urlpatterns = [
    path('users/', views.Authenticate.as_view(), name='users'),
    path('login/', views.Login.as_view(), name='login'),
]