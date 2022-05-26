from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import UserIsWorkingInTheSameCompany

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [UserIsWorkingInTheSameCompany, IsAuthenticated]