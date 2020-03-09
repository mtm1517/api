
from django.urls import path
from rest_framework import routers
from django.urls import include
from .views import CatelogyViewSet, ProductViewSet, ShippingViewSet, OrderViewSet, RatingViewSet, UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('catelogy', CatelogyViewSet)
router.register('product', ProductViewSet)
router.register('shipping', ShippingViewSet)
router.register('order', OrderViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]