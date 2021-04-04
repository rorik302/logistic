from rest_framework.routers import SimpleRouter

from companies.views import CompanyViewSet, CompanyTypeViewSet, RequisitesViewSet

app_name = 'companies'

router = SimpleRouter()
router.register('requisites', RequisitesViewSet)
router.register('types', CompanyTypeViewSet)
router.register('', CompanyViewSet)

urlpatterns = []
urlpatterns += router.urls
