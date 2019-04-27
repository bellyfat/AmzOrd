from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('totalsChart', views.orderCount, name='order count'),
    path('createOrder', views.orderCreateView, name='order create'),
]
