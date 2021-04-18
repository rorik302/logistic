from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):
    is_active = SerializerMethodField()

    def get_is_active(self, obj):
        return obj.is_active
