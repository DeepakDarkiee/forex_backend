from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.conf.urls.static import static

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="FOREX BACKEND API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=(f"{settings.URL}/"),
)

def trigger_error(request):
    try:
       division_by_zero = 1 / 0
    except:
        division_by_zero = "Hello World"

    return HttpResponse(division_by_zero)

urlpatterns = [
    path("admin_tools_stats/", include("admin_tools_stats.urls")),
    path("admin/", admin.site.urls),
    path("api/account/", include("accounts.urls")),
    path("api/journal/", include("journal.urls")),
    path("api/editorial/", include("editorial.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('sentry-debug/', trigger_error),
]

urlpatterns += [
    path(
        "swagger(?P<format>\.json|\.yaml)",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)