
from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

class Services(models.Model):
    title=models.CharField(max_length=200, verbose_name="Titulo")
    subtitle=models.CharField(max_length=200, verbose_name="Subtitulo")
    content=RichTextField(verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen", upload_to="services")
    created= models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")  #toma fecha del momento en que se crea         #es necesario agregar estos campos de creacion y actualizacion por buenas practicas
    updated= models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")      #cambia segun las actualizaciones


    class Meta: #modificaciones extendidas del modelo: cambiar nombre, ordenar registros etc
        verbose_name="servicio"
        verbose_name_plural="servicios"
        ordering=["created"] #- ordena desde el ultimo que se creo hasta el mas antiguo

    def __str__(self): # metodo srt --> retorna en forma de string la informacion del objeto
        return self.title
