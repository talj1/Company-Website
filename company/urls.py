from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from company.people.views import generate_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('generate-image/', generate_image, name="generate-image"),
    path('', TemplateView.as_view(template_name="index.html"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
