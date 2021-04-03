from django.urls import path

from companies.views import CompanyListCreateAPIView

urlpatterns = [
    path('', CompanyListCreateAPIView.as_view(), name='list_create_companies')
]
