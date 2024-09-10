from django.urls import path
from .import views

urlpatterns = [
    path('registation/', views.Registation.as_view(), name='users'),
    path('login/', views.Login.as_view(), name='login'),
]