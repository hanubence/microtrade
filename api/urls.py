from django.urls import path
from api.views import CompanyView

urlpatterns = [
    path("company/", CompanyView.as_view(), name="company"),
]
