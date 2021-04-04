from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'slug'
