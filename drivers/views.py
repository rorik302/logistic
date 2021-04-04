from rest_framework.viewsets import ModelViewSet

from drivers.models import Driver
from drivers.serializers import DriverSerializer


class DriverViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_field = 'slug'
