from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PerfumeViewSet

router = DefaultRouter()
router.register(r'perfumes', PerfumeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]