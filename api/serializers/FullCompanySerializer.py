from rest_framework import serializers
from rest_framework.serializers import ValidationError
from api.models import Company, Employee
from .CompanySerializer import CompanySerializer
from .EmployeeSerializer import EmployeeSerializer


class FullCompanySerializer(serializers.Serializer):
    company = CompanySerializer()
    employees = EmployeeSerializer(many=True, min_length=1, max_length=100)

    def create(self, validated_data):
        employees_data = validated_data.pop("employees")
        company_data = validated_data.pop("company")

        company = Company.objects.create(**company_data)

        for employee_data in employees_data:
            Employee.objects.create(company=company, **employee_data)

        return company

    def to_representation(self, instance):
        employees = EmployeeSerializer(
            instance=instance.employees.all(), many=True
        ).data
        return {
            "company": {
                "name": instance.name,
                "email": instance.email,
                "description": instance.description,
                "employees": employees,
            },
        }
