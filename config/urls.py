from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('subscriptions.urls')),
    path('', include(tf_urls)),
]
