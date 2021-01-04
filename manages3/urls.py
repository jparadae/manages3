"""Manages3 URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import url, include
from simpleDos.models import Cuenta,Accion, Proceso
from rest_framework import routers, serializers, viewsets



# Serializers define the API representation.
class CuentaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuenta
        fields = ('nombre', 'nombre_largo', 'metadata', 'mensaje', 'logo','favicon','api_token','descarga_masiva','client_id','client_secret','ambiente','vinculo_produccion','created_at','updated_at','entidad','estilo','header','footer','personalizacion','personalizacion_estado','seo_tags','analytics' )


# ViewSets define the view behavior.
class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer



class AccionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Accion
        fields = ('nombre', 'tipo', 'extra', 'proceso', 'exponer_variable')   


# ViewSets define the view behavior.
class AccionViewSet(viewsets.ModelViewSet):
    queryset = Accion.objects.all()
    serializer_class = AccionSerializer


class ProcesoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proceso
        fields = ('nombre', 'descripcion', 'url_informativa','usuario_id','created_at','updated_at', 'width', 'height','cuenta','proc_cont','activo','categoria_id','destacado','icon_ref','version','root','estado','concurrente','eliminar_tramites','ocultar_front', 'ficha_informativa','ficha_titulo','ficha_contenido')  


# ViewSets define the view behavior.
class ProcesoViewSet(viewsets.ModelViewSet):
    queryset = Proceso.objects.all()
    serializer_class = ProcesoSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cuenta', CuentaViewSet)
router.register(r'accion', AccionViewSet)
router.register(r'proceso', ProcesoViewSet)


urlpatterns = [
   path('admin/', admin.site.urls),

   #Paths de users
   path('', include(('users.urls', 'users'), namespace='users')),
   
   url(r'^', include(router.urls)),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))


   #
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)