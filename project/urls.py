from django.contrib import admin
from django.urls import path, include

from project.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/companies/', include('companies.urls')),
    path('api/drivers/', include('drivers.urls')),
]

if DEBUG:
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
        path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
