from rest_framework.test import APIRequestFactory, force_authenticate

from employees.models import Employee
from employees.views import create_user

username = "testUserForTestingAndItWillBeDeleted"
password = "12345678910"

user = Employee.objects.get(username="admin")

factory = APIRequestFactory()
request = factory.post('/create-user/', {
    "username": username,
    "password": password,
    "password2": password,
    "company": 1,
    "position": 2
} )

force_authenticate(request, user=user, token=user.auth_token)
create_user(request)

employees = Employee.objects.filter(username=username)

assert employees.exists(), ("The user " 
                             "couldn't be "
                              "created." )
employees.delete()                                                         