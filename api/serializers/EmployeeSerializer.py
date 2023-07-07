from rest_framework import serializers
from api.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["name", "email", "jobTitle", "age"]

    def create(self, validated_data):
        company = self.context.get("company")
        return Employee.objects.create(company=company, **validated_data)
