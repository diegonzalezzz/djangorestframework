from django.urls import path, include
from rest_framework import routers
from canciones import views

router = routers.DefaultRouter()
router.register(r'canciones', views.CancionView, 'canciones')

urlpatterns = [
    path('api/', include(router.urls))
]