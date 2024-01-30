from django.urls import path, include
from .views import index, cadastro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('cadastro', cadastro, name='cadastro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
