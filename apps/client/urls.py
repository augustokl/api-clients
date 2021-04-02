from django.urls import path, include
from client import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clients', views.ClientsViewSet, basename='Clients')

app_name = 'client'

urlpatterns = [
    path('', include(router.urls)),
]
