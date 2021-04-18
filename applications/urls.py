from rest_framework.routers import SimpleRouter

from applications.views import ApplicationViewSet

app_name = 'applications'

router = SimpleRouter()
router.register('', ApplicationViewSet)

urlpatterns = []
urlpatterns += router.urls
