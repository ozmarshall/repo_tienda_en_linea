from unicodedata import category
from django.db import models

class Etiqueta(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.CharField(max_length=20, unique=True, null=False)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now=True, db_column='updated_at')

    class Meta:
        db_table = 'etiquetas'
        ordering = ['-nombre']

class Tareas(models.Model):

    class CategoriaOpciones(models.TextChoices):
        TODO = 'TODO', 'TO_DO'
        IN_PROGRESS = 'IP', 'IN_PROGRESS'
        DONE = 'DONE', 'DONE'
        CANCELLED = 'CANCELLED', 'CANCELLED'

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    categoria = models.CharField(max_length=45, choices=CategoriaOpciones.choices, default=CategoriaOpciones.TODO)
    
    fechasCaducidad= models.DateTimeField(db_column='fecha_caducidad')
    importancia= models.IntegerField(null=False)
    descripcion = models.TextField(null=True)

    createdAt = models.DateTimeField(auto_now_add=True, db_column='created_at')
    updatedAt = models.DateTimeField(auto_now_add=True, db_column='update_at')

    etiquetas = models.ManyToManyField(to=Etiqueta, related_name='tareas')
    
    foto = models.ImageField(
        upload_to= 'multimedia',
        #height_field=200,
        #with_field
        null= True
    )



    class Meta:
        db_table = 'tareas'

