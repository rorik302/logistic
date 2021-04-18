from rest_framework.routers import SimpleRouter

from drivers.views import DriverViewSet, DriverPhoneViewSet, DriverLicenseViewSet, DriverPassportViewSet

router = SimpleRouter()
router.register('licenses', DriverLicenseViewSet)
router.register('passports', DriverPassportViewSet)
router.register('phones', DriverPhoneViewSet)
router.register('', DriverViewSet)

urlpatterns = []
urlpatterns += router.urls
