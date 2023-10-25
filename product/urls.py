from django.urls import path, include
from .views import CategoryView, ProductView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('categories', CategoryView)
router.register('products', ProductView)

urlpatterns = [
    path('', include(router.urls))
]