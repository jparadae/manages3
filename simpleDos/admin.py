#Registrando el modelo PerfilUsuario en el Admin de Django

#From Django
from django.contrib import admin
from simpleDos.models import Cuenta, Proceso, Accion
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User

"""
Aquí se registran los modelos que se deseen disponibilizar para el 
¿Digitalizador?Diego?

1. La información que desee mostrar es solo de lectura, para forzar a que dejen de usar de apoco simple2, 

"""

#Registrando tabla cuenta en el admin de django de forma custom
@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    """"
    search_field= busca entre el modelo usuario que extiende del auth de django
    list_filter = proporciona un filtro al modelo registrado 
    fieldset = dispone los campos a mostrar en el admin de perfilusuario segun la doc de django
    """
    list_display = ('pk','nombre', 'nombre_largo', 'mensaje')
    list_display_links = ('pk','nombre', 'nombre_largo','mensaje')
    #list_editable =('usuario','telefono') solo si quieres que sea editable inmediato 
   
    fieldsets = (
        (
            ("Datos Cuenta", {
                'fields':(('nombre','nombre_largo', 'mensaje')),
               
                
            }),
              ("Información Adicional", {
                'fields':(('api_token'),('vinculo_produccion'),)
                
            }),

            ("Clave unica", {
                'fields':(('client_id'),('client_secret'),)
                
            }),

       )
    )

    readonly_fields = ('nombre', 'nombre_largo','mensaje','vinculo_produccion','client_id','client_secret','api_token')

class CuentaInline(admin.StackedInline):
    """Se añade el perfil de usuario al momento de añadir un usuario en el admin de django"""

    model = Cuenta
    can_delte = False
    verbose_name_plural = 'roles'


#Registrando tabla Proceso en el admin de django de forma custom
@admin.register(Proceso)
class ProcesoAdmin(admin.ModelAdmin):
    """"
    search_field= busca entre el modelo usuario que extiende del auth de django
    list_filter = proporciona un filtro al modelo registrado 
    fieldset = dispone los campos a mostrar en el admin de perfilusuario segun la doc de django
    """
    list_display = ('pk','nombre', 'usuario_id','created_at','activo')
    list_display_links = ('pk','nombre','usuario_id','created_at','activo')
    #list_editable =('usuario','telefono') solo si quieres que sea editable inmediato 
   
    fieldsets = (
        (
            ("Datos Proceso", {
                'fields':(('nombre','descripcion')),
               
                
            }),
        

            ("Información Adicional", {
                'fields':(('ficha_titulo'),('destacado'),)
                
            }),

            ("Metadata", {
                'fields':(('created_at'), ('updated_at'),)
                
            }),

       )
    )

    readonly_fields = ('created_at', 'updated_at','nombre','descripcion', 'ficha_titulo','destacado')    


class ProcesoInline(admin.StackedInline):
    """Se añade el perfil de usuario al momento de añadir un usuario en el admin de django"""

    model = Proceso
    can_delte = False
    verbose_name_plural = 'procesos'    

class UserAdmin(BaseUserAdmin):
    """Se añade el perfil de usuario al momento de añadir un usuario en el admin de django"""
    
    inlines = (CuentaInline, ProcesoInline)

#admin.site.unregister(User)  