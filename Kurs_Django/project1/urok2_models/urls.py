from django.urls import path
from .views import Template_ViewLastOrders, Template_ViewAllProducts, Template_ProductImageSet

urlpatterns = [
    path('user_orders/', Template_ViewLastOrders.as_view(), name='user_orders'),
    path('user_orders/<int:user_id>/', Template_ViewLastOrders.as_view(), name='user_orders'),
    path('user_orders/<int:user_id>/<str:period>/', Template_ViewLastOrders.as_view(), name='user_orders'),
    path('products/', Template_ViewAllProducts.as_view(), name='products'),
    path('products/set_image', Template_ProductImageSet.as_view(), name='set_image'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static.files_urlpatterns()