from rest_framework.viewsets import ModelViewSet

from drivers.models import Driver, DriverPhone, DriverLicense, DriverPassport
from drivers.serializers import DriverSerializer, DriverPhoneSerializer, DriverLicenseSerializer, \
    DriverPassportSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'slug'


class DriverPhoneViewSet(ModelViewSet):
    queryset = DriverPhone.objects.all()
    serializer_class = DriverPhoneSerializer


class DriverLicenseViewSet(ModelViewSet):
    queryset = DriverLicense.objects.all()
    serializer_class = DriverLicenseSerializer


class DriverPassportViewSet(ModelViewSet):
    queryset = DriverPassport.objects.all()
    serializer_class = DriverPassportSerializer
