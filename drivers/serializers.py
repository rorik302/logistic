from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField

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
    phones = SerializerMethodField()

    class Meta:
        model = Driver
        fields = BaseModelSerializer.Meta.fields + ['company', 'full_name', 'phones', 'licenses', 'passports']

    def get_phones(self, obj):
        return DriverPhoneSerializer(obj.phones.all(), many=True).data

    def validate(self, attrs):
        company = attrs.get('company')
        if not company.is_transporter:
            raise ValidationError('Компания не может выступать в роли перевозчика')
        return attrs
