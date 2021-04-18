from rest_framework.viewsets import ModelViewSet

from applications.models import Application
from applications.serializers import ApplicationSerializer


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
