from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RolViewSet, UserViewSet, VentaViewSet

router = DefaultRouter()
router.register(r'roles', RolViewSet)
router.register(r'usuarios', UserViewSet)
router.register(r'ventas', VentaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]