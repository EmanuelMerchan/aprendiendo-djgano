from django.db import models
from ckeditor.fields import RichTextField

# Modelo de página
class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Título")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")
    visible = models.BooleanField(verbose_name="¿Visible?")
    order = models.IntegerField(default=0, verbose_name="Orden")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualización")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title