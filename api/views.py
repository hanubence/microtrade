from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Company
from api.serializers import CompanySerializer


class CompanyListCreateView(ListCreateAPIView):
    def get(self, request):
        company_serializer = CompanySerializer(Company.objects.all(), many=True)

        return Response(company_serializer.data)

    def post(self, request):
        data = request.data
        data["company"]["employees"] = data.pop("employees")
        company_serializer = CompanySerializer(data=data["company"])

        if company_serializer.is_valid(raise_exception=True):
            company_serializer.save()

        return Response(data)
