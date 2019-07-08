from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='inicio'),
    path('login', auth_views.login, name='login'),
    path('registro/', views.signup, name='signup'),
    path('servicio',views.servicios,name='serviciosDatos'),
    path('servicio2',views.servicios2,name='servicios2'),
    path('catalogo',views.catalogo,name='catalogo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)