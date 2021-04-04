from django.urls import path

from companies.views import CompanyListCreateAPIView, CompanyRUDAPIView

app_name = 'companies'

urlpatterns = [
    path('<slug:slug>/', CompanyRUDAPIView.as_view(), name='rud_company'),
    path('', CompanyListCreateAPIView.as_view(), name='list_create_companies')
]
