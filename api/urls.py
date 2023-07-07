from django.urls import path
from api.views import CompanyListCreateView

urlpatterns = [path("company/", CompanyListCreateView.as_view(), name="company")]
