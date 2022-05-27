from django.db import models
from cloudinary import models as modelsCloudinary

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    image = modelsCloudinary.CloudinaryField(folder='usuario')
    name = models.CharField(max_length=45, null=False)
    lastname = models.CharField(max_length=45, null=False)
    alias = models.CharField(max_length=45, null=False)
    phone = models.CharField(max_length=45, null=False)
    document = models.CharField(max_length=45, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    confirmpassword = models.TextField(null=False)
    description = models.CharField(max_length=200, null=False)
    

    def __str__(self):
        return self.tittle
    
  
        

