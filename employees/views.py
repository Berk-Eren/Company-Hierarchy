from .models import Employee
from .serializers import EmployeeSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.shortcuts import render


@api_view(['POST', 'GET'])
@permission_classes([IsAdminUser])
def create_user(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        instance = serializer.save()
        Token.objects.get_or_create(user=instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomObtainToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, 
                                            context={"request": request})
        
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                'token': token.key,
                'company': user.company.title if user.company else user.company,
                'position': user.position.title if user.position else user.position,
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)