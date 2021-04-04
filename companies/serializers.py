from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from companies.models import Company, CompanyType, Requisites


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, attrs):
        is_own = attrs.get('is_own')
        is_customer = attrs.get('is_customer')
        is_transporter = attrs.get('is_transporter')

        if not is_own and not is_transporter and not is_customer:
            raise ValidationError('Нужно указать is_customer или is_transporter')

        if self.instance and self.instance.requisites.count() > 0:
            if not self.instance.requisites.filter(is_active=True).exists():
                raise ValidationError('Нужно указать актуальные реквизиты')
            if self.instance.requisites.filter(is_active=True).count() > 1:
                raise ValidationError('Актуальные реквизиты должны быть только одни')
        return attrs


class CompanyTypeSerializer(ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'

    def validate(self, attrs):
        name_short = attrs.get('name_short')
        name_full = attrs.get('name_full')

        errors = {}

        instance_id = self.instance.id if self.instance else None

        if CompanyType.objects.filter(name_short=name_short).exclude(id=instance_id).exists():
            errors['name_short'] = 'Правовая форма уже существует'

        if CompanyType.objects.filter(name_full=name_full).exclude(id=instance_id).exists():
            errors['name_full'] = 'Правовая форма уже существует'

        if bool(errors):
            raise ValidationError(errors)

        return attrs


class RequisitesSerializer(ModelSerializer):
    class Meta:
        model = Requisites
        fields = '__all__'
