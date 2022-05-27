from django.db import models
from cloudinary import models as modelsCloudinary

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    numberItem = models.CharField(max_length=45, null=False)
    contac = models.CharField(max_length=45, null=False)
    phoneNumber = models.CharField(max_length=45, null=False)
    image = modelsCloudinary.CloudinaryField(folder='articulo')
    description = models.CharField(max_length=200, null=False)
    price = models.FloatField(null=False)
    paymentMeth = models.CharField(max_length=45, null=False)
    receptionN = models.CharField(max_length=45, null=False)
    stateRanking = models.CharField(max_length=45, null=False)
    stateS = models.IntegerField()
    tittle = models.CharField(max_length=45, null=False)
    typeCurrency = models.CharField(max_length=45, null=False)

    def __str__(self):
        return self.tittle
    
  
        
