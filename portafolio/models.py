from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField( upload_to='proyectos')
    enlace = models.URLField(null=True,blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    # luego hay que crear la migracion
    # python. manage.py makemigrations app
    # python manage.py migrate app

    class Meta:
        ordering = ['-creado']
    
    def __str__(self):
        return self.titulo
    