from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jazzyburger.views import ProductViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)