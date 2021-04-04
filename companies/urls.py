from django.urls import path

from companies.views import CompanyListCreateAPIView, CompanyRUDAPIView, CustomerListAPIView, TransporterListAPIView, \
    OwnCompanyListAPIView

app_name = 'companies'

urlpatterns = [
    path('customers/', CustomerListAPIView.as_view(), name='customers'),
    path('own/', OwnCompanyListAPIView.as_view(), name='own_companies'),
    path('transporters/', TransporterListAPIView.as_view(), name='transporters'),
    path('<slug:slug>/', CompanyRUDAPIView.as_view(), name='rud_company'),
    path('', CompanyListCreateAPIView.as_view(), name='list_create_companies')
]
