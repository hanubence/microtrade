from rest_framework import serializers
from rest_framework.serializers import ValidationError
from api.models import Company, Employee
from .EmployeeSerializer import EmployeeSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["name", "email", "description"]
