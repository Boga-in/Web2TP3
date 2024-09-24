from django.urls import path
from .views import CrearPostView, index, RegistroUsuarioView, LoginUsuarioView, LogoutUsuarioView
from .views import (ListaPublicacionesView, DetallePublicacionView, EliminarPublicacionView, EditarPublicacionView)
app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('crear/', CrearPostView.as_view(), name='crear_post'),
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginUsuarioView.as_view(), name='login'),  # Ruta para el login
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
    path('lista_publicaciones/', ListaPublicacionesView.as_view(), name='lista_publicaciones'),
    path('publicacion/<int:pk>/', DetallePublicacionView.as_view(), name='detalle_publicacion'),
    path('publicacion/<int:pk>/eliminar/', EliminarPublicacionView.as_view(), name='eliminar_publicacion'),
    path('publicacion/<int:pk>/editar/', EditarPublicacionView.as_view(), name='editar_publicacion'),
]