from rest_framework import exceptions
from rest_framework import authentication

from .models import Employee


class IncludesHeaderForUserCreationAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        company_token = request.GET.get('Company-Application-Id')
        