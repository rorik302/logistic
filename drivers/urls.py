from rest_framework.routers import SimpleRouter

from drivers.views import DriverViewSet

router = SimpleRouter()
router.register('', DriverViewSet)

urlpatterns = []
urlpatterns += router.urls
