from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from companies.models import Company, CompanyType, Requisites
from companies.serializers import CompanySerializer, CompanyTypeSerializer, RequisitesSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'slug'

    @action(methods=['GET'], detail=False)
    def customers(self, request):
        customers = Company.objects.filter(is_customer=True)
        serializer = self.get_serializer(customers, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def transporters(self, request):
        transporters = Company.objects.filter(is_transporter=True)
        serializer = self.get_serializer(transporters, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False)
    def own(self, request):
        own_companies = Company.objects.filter(is_own=True)
        serializer = self.get_serializer(own_companies, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def requisites(self, request, slug):
        company = self.get_object()
        serializer = RequisitesSerializer(company.requisites.all(), many=True)
        return Response(serializer.data)


class CompanyTypeViewSet(ModelViewSet):
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeSerializer
    lookup_field = 'slug'


class RequisitesViewSet(ModelViewSet):
    queryset = Requisites.objects.all()
    serializer_class = RequisitesSerializer
    lookup_field = 'slug'
