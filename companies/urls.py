import companies.viewsets as viewsets

from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()
router.register('companies', viewsets.CompanyViewSet)

urlpatterns = router.urls