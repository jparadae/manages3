#Registrando el modelo PerfilUsuario en el Admin de Django

#From Django
from django.contrib import admin
from users.models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

"""Registrando el modelo Perfil de la forma tradicional al admin de django
admin.site.register(UserProfile)
"""

#Registrando el Perfil en el admin de django de forma custom
@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    """"
    Clase que lista más opciones de un perfil que las de default de django,
    tambien genera listas desplegables para editar inmediatamente sin tener que acceder al elemento
    list_editable = dentro de los elementos de la lista da la opcion de editar sin tener que acceder
    al elemento.
    search_field= busca entre el modelo usuario que extiende del auth de django
    list_filter = proporciona un filtro al modelo registrado 
    fieldset = dispone los campos a mostrar en el admin de perfilusuario segun la doc de django
    """
    list_display = ('pk','usuario', 'rut','telefono', 'backend', 'frontend', 'registrado')
    list_display_links = ('pk','usuario', 'rut','telefono', 'backend', 'frontend', 'registrado')
    #list_editable =('usuario','telefono') solo si quieres que sea editable inmediato 
    search_fields = (
    'usuario__first_name',
     'usuario__last_name', 
     'usuario__username')
    list_filter = (
     'backend', 
     'frontend',
     'registrado',
     'updated_at' )

    fieldsets = (
        (
            ("Datos Usuario", {
                'fields':(('usuario','rut','registrado')),
               
                
            }),

            ("Rol Usuario", {
                'fields':(('backend', 'frontend')),
               
                
            }),


            ("Información Adicional", {
                'fields':(('img_perfil'),('telefono'),)
                
            }),

            ("Metadata", {
                'fields':(('created_at'), ('updated_at'),)
                
            }),
       )
    )

    readonly_fields = ('created_at', 'updated_at','registrado')

class ProfileInline(admin.StackedInline):
    """Se añade el perfil de usuario al momento de añadir un usuario en el admin de django"""

    model = UserProfile
    can_delte = False
    verbose_name_plural = 'roles'

class UserAdmin(BaseUserAdmin):
    """Se añade el perfil de usuario al momento de añadir un usuario en el admin de django"""
    
    inlines = (ProfileInline)

admin.site.unregister(User)    
#admin.site.register(User, UserAdmin)