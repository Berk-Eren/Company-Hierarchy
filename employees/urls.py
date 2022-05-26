import employees.views as views
import employees.viewsets as viewsets

from django.urls import path
from rest_framework import routers


router = routers.SimpleRouter()
router.register('employees', viewsets.EmployeeViewSet)

urlpatterns = [path('create-user/', views.create_user)] + router.urls