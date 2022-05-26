import positions.viewsets as viewsets

from rest_framework import routers
from django.urls import path


router = routers.SimpleRouter()
router.register('positions', viewsets.PositionViewSet, basename='position')

urlpatterns = router.urls