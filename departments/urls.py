import departments.viewsets as viewsets

from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()
router.register('departments', viewsets.DepartmentViewSet, basename='department')

urlpatterns = router.urls