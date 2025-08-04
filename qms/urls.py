from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index,admin, queue_users, QueueUserViewSet, QueueItemViewSet

router = DefaultRouter()
router.register(r'users', QueueUserViewSet)
router.register(r'items', QueueItemViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin, name='admin'),
    path('queue/users/', queue_users, name='queue_users'),
    path('api/queue/', include(router.urls)),
    ]