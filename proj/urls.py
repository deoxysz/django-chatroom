from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('social.urls')),
    path('api/', include('social.api.urls'))
]
