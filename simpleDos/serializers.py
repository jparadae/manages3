from django.conf.urls import url, include
from simpleDos.models import Cuenta, Accion, Acontecimiento,CuentaHasConfig
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


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'cuenta', CuentaViewSet)
