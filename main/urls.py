from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title='Python 25 Blog',
        default_version='v1',
        description='blog'
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/post/', include('applications.post.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
