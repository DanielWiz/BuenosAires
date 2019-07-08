from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .models import Servicios, Catalogo
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class ServiciosSerializer(serializers.HyperlinkedModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Servicios
		fields = ('Usuario', 'Nombres', 'Email', 'Telefono', 'Ubicacion', 'ZipCode', 'Fecha', 'url')
		
class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CatalogoSerializer(serializers.HyperlinkedModelSerializer):
	"""docstring for ClassName"""
	class Meta:
		model = Catalogo
		fields = ('Nombre', 'Imagen', 'Stock', 'url')
		
class CatalogoViewSet(viewsets.ModelViewSet):
    queryset =Catalogo.objects.all()
    serializer_class = CatalogoSerializer

router = routers.DefaultRouter()
router.register('servicios', ServiciosViewSet)
router.register('users', UserViewSet)
router.register('Catalogo', CatalogoViewSet)

urlpatterns = [
    path('', views.index, name='inicio'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('registro/', views.signup, name='signup'),
    path('servicio',views.servicios,name='serviciosDatos'),
    path('servicio2',views.servicios2,name='servicios2'),
    path('catalogo',views.catalogo,name='catalogo'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('mi-api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)