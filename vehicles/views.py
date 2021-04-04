from rest_framework.viewsets import ModelViewSet

from vehicles.models import Vehicle
from vehicles.serializers import VehicleSerializer


class VehicleViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = 'slug'
