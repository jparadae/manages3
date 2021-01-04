"""URL Usuarios"""

#From django
from django.urls import path
from django.views.generic import TemplateView
#From users
from users import views

urlpatterns=[

   path(
       route='users/login/', 
       view=views.LoginView.as_view(), 
       name='login'),

   path(
       route='users/salir/', 
       view=views.LogoutView.as_view(), 
       name='salir'),

   path(
       route='users/edit/profile',
       view=views.EditarPerfil.as_view(), 
       name='editar_perfil'),

   path(
       route='users/index/',
       view=views.IndexViews.as_view(), 
       name='index'),     

    #Django resuelve por orden las urls
    
    path(
       route='usuario/<str:usuario>/',
       view=views.DetalleUsuario.as_view(),
       name='detalle'),   
  
]
