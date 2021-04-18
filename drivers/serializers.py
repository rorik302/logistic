from rest_framework.exceptions import ValidationError

from drivers.models import Driver, DriverPhone, DriverLicense, DriverPassport
from project.base.serializers import BaseModelSerializer


class DriverPhoneSerializer(BaseModelSerializer):
    class Meta:
        model = DriverPhone
        fields = '__all__'


class DriverLicenseSerializer(BaseModelSerializer):
    class Meta:
        model = DriverLicense
        fields = '__all__'


class DriverPassportSerializer(BaseModelSerializer):
    class Meta:
        model = DriverPassport
        fields = '__all__'


class DriverSerializer(BaseModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

    def validate(self, attrs):
        company = attrs.get('company')
        if not company.is_transporter:
            raise ValidationError('Компания не может выступать в роли перевозчика')
        return attrs
