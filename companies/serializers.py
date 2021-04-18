from companies.models import Company, CompanyType, Requisites
from project.base.serializers import BaseModelSerializer


class CompanySerializer(BaseModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyTypeSerializer(BaseModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'


class RequisitesSerializer(BaseModelSerializer):
    class Meta:
        model = Requisites
        fields = '__all__'
