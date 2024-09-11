from django.urls import path
from .import views

urlpatterns = [
    path('order/', views.OrderListView.as_view(), name='orders'),
    path('userandorder/', views.OrderDetailView.as_view(), name='userandorders'),
]