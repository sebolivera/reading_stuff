from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('userauth.urls')),
    path('', include('readwrite.urls')), #last bc posts can have any url atm 
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += i18n_patterns(
#     path('', include('userauth.urls')),
#     path('', include('readwrite.urls')),
#     path('ckeditor/', include('ckeditor_uploader.urls')),
#     prefix_default_language=False
#  ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
