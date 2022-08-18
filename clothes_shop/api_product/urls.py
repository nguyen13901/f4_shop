from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_product import views

router = DefaultRouter()
router.register(r'products', views.ProductView, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]