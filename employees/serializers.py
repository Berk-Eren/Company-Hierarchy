from .models import Employee

from rest_framework import serializers
from django.contrib.auth.hashers import PBKDF2PasswordHasher


class EmployeeSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, 
                                        style={"input_type": "password"} )
    job = serializers.SerializerMethodField(read_only=True)
    company_name = serializers.StringRelatedField(source="company")
    position_name = serializers.StringRelatedField(source="company")

    class Meta:
        model = Employee
        fields = ['username', 'position_name', 'company_name', 
                    'job', 'email', 'password2', 'password', 'date_joined', 
                      'company', 'position', ]
        read_only_fields = ['date_joined', ]
        extra_kwargs = {
            'company': {'write_only': True},
            'position': {'write_only': True},
            'password': {'write_only': True}
        }

    def save(self, *args, **kwargs):
        del self.validated_data["password2"]

        password_hasher = PBKDF2PasswordHasher()
        self.validated_data["password"] = password_hasher.encode(
                                              self.validated_data["password"],
                                               password_hasher.salt() 
                                            )
        
        return super().save(*args, **kwargs)

    def validate(self, validated_data):
        if self.initial_data["password"] != self.initial_data["password2"]:
            raise serializers.ValidationError(("Your 'password' is "
                                                "not equal to 'password2'.") )
        return validated_data

    def get_job(self, obj):
        pre_text = ""

        if obj.position:
            pre_text += obj.position.title
        if obj.company:
            pre_text += " in " + obj.company.title
        if not pre_text:
            pre_text = "Unemployed"

        return pre_text