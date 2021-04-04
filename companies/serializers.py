from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer

from companies.models import Company


class CompanySerializer(ModelSerializer):
    uri = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'

    def get_uri(self, object):
        return reverse('companies:rud_company', request=self.context.get('request'), kwargs={'slug': object.slug})

    def validate(self, attrs):
        is_own = attrs.get('is_own')
        if not is_own:
            is_customer = attrs.get('is_customer')
            is_transporter = attrs.get('is_transporter')
            if not is_customer and not is_transporter:
                raise ValidationError('Нужно указать is_customer или is_transporter или оба')
        return attrs
