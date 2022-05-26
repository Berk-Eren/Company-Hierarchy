from .models import Company
from .serializers import CompanySerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.permissions import ReadOnly


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsAuthenticated|ReadOnly] # IsAuthenticated or ReadOnly permission
    filterset_fields = ['title', ]