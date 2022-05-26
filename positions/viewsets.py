from .serializers import PositionSerializer
from .models import Position
from .permissions import PositionIsPartOfTheCompany
from .filters import PositionDepartmentTogetherFilter

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
    permission_classes = [PositionIsPartOfTheCompany, IsAuthenticated]
    filter_backends = [PositionDepartmentTogetherFilter]
    allowed_fields = ["position", "department", ]

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return Position.objects.all()
        
        return Position.objects.filter(department__company=self.request.user.company)