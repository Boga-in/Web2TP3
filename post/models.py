from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField(max_length=150)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_publicado')

    def __str__(self):
        return f"{self.titulo} de {self.autor}: {self.contenido}"
