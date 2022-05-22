from django.db import models
from cloudinary import models as modelsCloudinary

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, null=False)
    foto = modelsCloudinary.CloudinaryField(folder='articulo')
    disponible = models.BooleanField(default=True, null=False)
    precio = models.FloatField(null=False)
    class Meta:
        db_table = 'articulos'
  
        
