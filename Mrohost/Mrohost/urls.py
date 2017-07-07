from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from hostapp import views
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$', views.home, name='main'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
