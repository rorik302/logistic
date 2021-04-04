from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from vehicles.models import Vehicle


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def validate(self, attrs):
        company = attrs.get('company')
        if not company.is_transporter:
            raise ValidationError('Компания не может выступать в роли перевозчика')

        type = attrs.get('type')
        mark = attrs.get('mark')

        if type == 'auto' and not mark:
            raise ValidationError('Нужно указать марку автомобиля')

        return attrs
