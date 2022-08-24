from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_account import views

router = DefaultRouter()
router.register(r'accounts', views.AccountViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls)),
]