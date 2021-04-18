from applications.models import Application
from project.base.serializers import BaseModelSerializer


class ApplicationSerializer(BaseModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
