import json

from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token

from companies.models import Company
from employees.models import Employee
from departments.models import Department


class DepartmentTests(APITestCase):

    def setUp(self):
        admin_user = Employee.objects.create(username="testadmin123", 
                                                password="testadmin123", 
                                                    is_superuser=True)
        
        self.admin_token = Token.objects.create(user=admin_user)
        
        self.client.credentials(
            HTTP_AUTHORIZATION="Custom %s" % self.admin_token.key
        )
        test_company_title = "TestCompany1234567890"
        self.test_company = Company.objects.create(title=test_company_title)

    def send_request(self, url, data=None):
        return self.client.post(url, data=data)

    def test_department_creation_is_succesful(self):
        test_department_title = "TestDepartment123456789"

        department_data = {
            "title": test_department_title,
            "company": self.test_company.id 
        }

        response = self.send_request('/departments/', department_data)
        
        self.assertEqual(response.status_code, 201)
        
        department = Department.objects.filter(title=test_department_title)
        is_department_exist = department.exists()
        
        try:
            self.assertEqual(is_department_exist, True)
            Department.objects.get(title=test_department_title).delete()
        except Exception as e:
            raise e

    def test_department_creation_with_missing_arguments(self):
        """
        Test for the following missing attributes:
            - title
            - company
        """

        # Company is missing
        test_department_title = "TestDepartment123456789"
        department_data = {
            "title": test_department_title
        }
        response = self.send_request('/departments/', department_data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.dumps(response.data), 
            '{"company": ["This field is required."]}'
        )

        # Title is missing
        department_data = {
            "company": -1
        }
        response = self.send_request('/departments/', department_data)
        breakpoint()
        self.assertEqual(response.status_code, 400)

        # Don't send data.
        response = self.send_request('/departments/')
        breakpoint()
        self.assertEqual(response.status_code, 400)
        
    def tearDown(self):
        self.test_company.delete()