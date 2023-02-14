from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    created= models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")  #toma fecha del momento en que se crea         #es necesario agregar estos campos de creacion y actualizacion por buenas practicas
    updated= models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")      #cambia segun las actualizaciones


    class Meta:
       verbose_name="pagina"
       verbose_name_plural="paginas"
       ordering=['created']

    def __str__(self):
       return self.title