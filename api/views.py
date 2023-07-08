from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from django.db.models import Q

from .models import Company
from api.serializers import CompanySerializer


class CompanyView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        name_param = self.request.query_params.get("name")
        ordering_param = self.request.query_params.get("order")

        queryset = Company.objects.all()

        if name_param is not None:
            queryset = queryset.filter(
                Q(name__icontains=name_param) | Q(email__icontains=name_param)
            )

        if ordering_param is not None:
            try:
                queryset = queryset.order_by(ordering_param)
            except:
                return queryset

        return queryset

    def post(self, request):
        data = request.data
        data["company"]["employees"] = data.pop("employees")
        company_serializer = CompanySerializer(data=data["company"])

        if company_serializer.is_valid(raise_exception=True):
            company_serializer.save()

        return Response(data)
