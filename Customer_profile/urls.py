from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Customer_profile import views

router = DefaultRouter()
router.register('Customer', views.CustomerViewSet, basename='Customer')

urlpatterns = [
    path('', include(router.urls)),
]
