from django.contrib import admin
from django.urls import path
from django.conf import settings
from SalonSamochodowyApp.views import cars
from django.conf.urls.static import static
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

 name=input('Piotr')

int('xyz')

nt('xyz')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', cars, name='cars'),
    path('sentry-debug/', trigger_error),
              ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
