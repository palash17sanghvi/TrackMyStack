from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboard/delete/<int:sub_id>/',
         views.delete_subscription_view, name='delete_subscription'),
    path('dashboard/update/<int:sub_id>/',
         views.update_subscription_view, name='update_subscription'),
]
