from django.urls import path
from .import views

urlpatterns = [
    path('order/', views.OrderListView.as_view(), name='orders'),
    path('order-v2/', views.OrderListViewV2.as_view(), name='orders-v2'),
    path('userandorder/', views.OrderDetailView.as_view(), name='userandorders'),
    path('factorial/<int:n>', views.factorial_with_cache.as_view(), name='factorial'),
]