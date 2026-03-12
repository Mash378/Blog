from django.urls import path
from rest_framework import routers
from .api_views import register_user
from .views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('register/', register_user),
]
urlpatterns += router.urls