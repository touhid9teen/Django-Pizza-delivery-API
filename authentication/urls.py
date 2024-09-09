from django.urls import path
from .import views

urlpatterns = [
    path('authenticate/', views.Authenticate.as_view(), name='authenticate'),
]