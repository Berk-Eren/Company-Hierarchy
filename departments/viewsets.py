from .models import Department
from .serializers import DepartmentSerializer
from .permissions import DepartmentIsPartOfTheCompany

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import AnonymousUser
from django_filters.rest_framework import DjangoFilterBackend


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [DepartmentIsPartOfTheCompany, IsAuthenticated]
    filterset_fields = ['title', ]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.is_staff:
            return Department.objects.all()

        return Department.objects.filter(company=user.company)