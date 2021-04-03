from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from companies.models import Company


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, attrs):
        is_own = attrs.get('is_own')
        if not is_own:
            is_customer = attrs.get('is_customer')
            is_transporter = attrs.get('is_transporter')
            if not is_customer and not is_transporter:
                raise ValidationError('Нужно указать is_customer или is_transporter или оба')
        return attrs
