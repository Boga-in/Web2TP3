from django.shortcuts import render
from .models import Post 
from .forms import PostForm, RegistroForm  
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, 'index.html')

    
class RegistroUsuarioView(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'registro.html'
    success_url = reverse_lazy('post:index')  # Redirige después de un registro exitoso

    def form_valid(self, form):
        # Guardar el usuario y luego autenticarlo y loguearlo automáticamente
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Autenticar y loguear automáticamente
        return response
    

class LoginUsuarioView(LoginView):
    template_name = 'login.html' 
    redirect_authenticated_user = True
    success_url = reverse_lazy('post:index') 

    def get_success_url(self):
        return self.success_url
    

class LogoutUsuarioView(LogoutView):
    next_page = reverse_lazy('post:index')  # Redirige después del logout


class CrearPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'crear_post.html'
    context_object_name = 'publicacion'
    success_url = reverse_lazy('post:index')

    # Asigna automáticamente el autor de la publicación al usuario autenticado
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditarPublicacionView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'editar_publicacion.html'
    context_object_name = 'publicacion'
    success_url = reverse_lazy('post:lista_publicaciones')

    # Verificar que el usuario autenticado es el autor
    def test_func(self):
        publicacion = self.get_object()
        return self.request.user == publicacion.autor

class ListaPublicacionesView(ListView):
    model = Post
    template_name = 'lista_publicaciones.html'
    context_object_name = 'publicaciones'
    ordering = ['-fecha_publicacion']

class DetallePublicacionView(DetailView):
    model = Post
    template_name = 'detalle_publicacion.html'
    context_object_name = 'publicacion'

class EliminarPublicacionView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'eliminar_publicacion.html'
    success_url = reverse_lazy('post:lista_publicaciones')

    # Este método se usa para verificar que el usuario autenticado es el autor de la publicación
    def test_func(self):
        publicacion = self.get_object()
        return self.request.user == publicacion.autor
    
