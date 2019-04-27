from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:order_id>/', views.detail, name='detail'),
    path('aPath', views.orderCount, name='order count'),
    path('<int:order_id>/result', views.result, name='result'),
    path('createOrder', views.orderCreateView, name='order create'),
]
