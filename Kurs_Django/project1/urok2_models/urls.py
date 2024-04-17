from django.urls import path
from .views import Template_ViewLastOrders

urlpatterns = [
    path('user_orders/', Template_ViewLastOrders.as_view(), name='user_orders'),
    path('user_orders/<int:user_id>/', Template_ViewLastOrders.as_view(), name='user_orders'),
    path('user_orders/<int:user_id>/<str:period>/', Template_ViewLastOrders.as_view(), name='user_orders'),
]

