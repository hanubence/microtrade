from rest_framework import serializers
from rest_framework.serializers import ValidationError
from api.models import Company, Employee
from .EmployeeSerializer import EmployeeSerializer


class CompanySerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, min_length=1, max_length=100)

    class Meta:
        model = Company
        fields = "__all__"

    def create(self, validated_data):
        employees_data = validated_data.pop("employees")

        company = Company.objects.create(**validated_data)

        for employee_data in employees_data:
            Employee.objects.create(company=company, **employee_data)

        return company
