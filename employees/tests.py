import json

from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token


from positions.models import Position
from companies.models import Company
from departments.models import Department
from employees.models import Employee


class EmployeeTests(APITestCase):

    def setUp(self):
        self.admin_user = Employee.objects.create(username="testadmin123", 
                                                    password="testadmin123", 
                                                        is_superuser=True,
                                                            is_staff=True )
        
        admin_token = Token.objects.create(user=self.admin_user)
        
        self.client.credentials(
            HTTP_AUTHORIZATION="Custom %s" % admin_token.key
        )

        # Create a company
        self.test_company = Company.objects.create(
                                title="TestCompany1234567890"
                            )

        # Create a department
        self.test_department = Department.objects.create(
                                    title="TestDepartment123456789",
                                    company=self.test_company
                                )

        # Create a position
        self.test_position = Position.objects.create(
                                    title="TestPosition123456789",
                                    department=self.test_department
                            )

    def send_request(self, url, data=None):
        return self.client.post(url, data)

    def test_employee_creation_is_succesful(self):
        username = "testUserForTestingAndItWillBeDeleted"
        password = "12345678910"

        data = {
            "username": username,
            "password": password,
            "password2": password,
            "company": self.test_company.id,
            "position": self.test_position.id
        }

        self.send_request('/create-user/', data)

        is_employee_exist = Employee.objects.filter(username=username).exists()
        
        try:
            self.assertEqual(is_employee_exist, True)
            Employee.objects.get(username=username).delete()
        except Exception as e:
            raise e

    def tearDown(self):
        self.admin_user.delete()