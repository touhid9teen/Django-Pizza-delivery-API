
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza/', include('orders.urls')),
    path('auth/', include('authentication.urls')),
]
