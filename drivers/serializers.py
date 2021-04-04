from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from drivers.models import Driver


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

    def validate(self, attrs):
        company = attrs.get('company')
        if not company.is_transporter:
            raise ValidationError('Компания не может выступать в роли перевозчика')
        return attrs
