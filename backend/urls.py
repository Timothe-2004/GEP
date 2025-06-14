from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/service/', include('service.urls')),
    path('api/agence/', include('agence.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/newsletter/', include('newsletter.urls')),
    path('api/partenaires/', include('partenaires.urls')),
    path('api/realisations/', include('realisations.urls')),
    path('api/stages/', include('stages.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui-alt'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]