#Registrando el modelo PerfilUsuario en el Admin de Django

#From Django
from django.contrib import admin
from simpleDos.models import Cuenta
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from django.contrib.auth.models import User

"""Registrando el modelo Perfil de la forma tradicional al admin de django
admin.site.register(UserProfile)
"""

#Registrando el Perfil en el admin de django de forma custom
@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    """"
    Clase que lista más opciones de un perfil que las de default de django,
    tambien genera listas desplegables para editar inmediatamente sin tener que acceder al elemento
    list_editable = dentro de los elementos de la lista da la opcion de editar sin tener que acceder
    al elemento.
    search_field= busca entre el modelo usuario que extiende del auth de django
    list_filter = proporciona un filtro al modelo registrado 
    fieldset = dispone los campos a mostrar en el admin de perfilusuario segun la doc de django
    """
    list_display = ('pk','nombre', 'nombre_largo')
    list_display_links = ('pk','nombre', 'nombre_largo')
    #list_editable =('usuario','telefono') solo si quieres que sea editable inmediato 
   
    fieldsets = (
        (
            ("Datos Cuenta", {
                'fields':(('nombre','nombre_largo')),
               
                
            }),

          

           
       )
    )

    #readonly_fields = ('created_at', 'updated_at','registrado')

class CuentaInline(admin.StackedInline):
    """Se añade el perfil de usuario al momento de añadir un usuario en el admin de django"""

    model = Cuenta
    can_delte = False
    verbose_name_plural = 'roles'

class UserAdmin(BaseUserAdmin):
    """Se añade el perfil de usuario al momento de añadir un usuario en el admin de django"""
    
    inlines = (CuentaInline)

#admin.site.unregister(User)  