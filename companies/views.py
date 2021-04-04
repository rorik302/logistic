from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'slug'


class CustomerListAPIView(ListAPIView):
    queryset = Company.objects.filter(is_customer=True)
    serializer_class = CompanySerializer


class TransporterListAPIView(ListAPIView):
    queryset = Company.objects.filter(is_transporter=True)
    serializer_class = CompanySerializer


class OwnCompanyListAPIView(ListAPIView):
    queryset = Company.objects.filter(is_own=True)
    serializer_class = CompanySerializer
