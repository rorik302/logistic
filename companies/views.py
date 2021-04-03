from rest_framework.generics import ListCreateAPIView

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
