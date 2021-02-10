from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from company.people import views as people_views
from company.products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people', people_views.view_people, name="people"),
    path('products', product_views.view_products, name="products"),
    path('generate-image/', people_views.generate_image, name="generate-image"),
    path('', TemplateView.as_view(template_name="index.html"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
