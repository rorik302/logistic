from django.urls import path

from companies.views import CompanyListCreateAPIView, CompanyRUDAPIView, CustomerListAPIView, TransporterListAPIView, \
    OwnCompanyListAPIView, CompanyTypeListCreateAPIView, CompanyTypeRUDAPIView

app_name = 'companies'

urlpatterns = [
    path('customers/', CustomerListAPIView.as_view(), name='list_customers'),
    path('own/', OwnCompanyListAPIView.as_view(), name='list_own_companies'),
    path('transporters/', TransporterListAPIView.as_view(), name='list_transporters'),
    path('types/<slug:slug>/', CompanyTypeRUDAPIView.as_view(), name='rud_type'),
    path('types/', CompanyTypeListCreateAPIView.as_view(), name='list_create_types'),
    path('<slug:slug>/', CompanyRUDAPIView.as_view(), name='rud_company'),
    path('', CompanyListCreateAPIView.as_view(), name='list_create_companies')
]
