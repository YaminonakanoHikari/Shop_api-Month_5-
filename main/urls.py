from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include


# --- Определяем функцию до urlpatterns ---
def home(request):
    return HttpResponse("Добро пожаловать в Shop API — используйте /api/v1/...")

urlpatterns = [
    path('', home),  # теперь Django знает, что такое home
    path('admin/', admin.site.urls),
    path('api/v1/', include('product.urls')),
]

# --- Подключаем статику и медиа ---
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
