from django.db import models

# Create your models here.
class category(models.Model):
    name =models.CharField(max_length=255)
    image =models.ImageField(upload_to='products/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Brand(models.Model):
        name = models.CharField (max_length=255)
        image = models.ImageField(upload_to='products/')
        description = models.TextField(blank=True, null=True)
    
    def __str__(self):
            return self.name
    
    class Product(models.Model):
         #cloth
         title = models.CharField(max_length=255)
         image = models.ImageField(upload_to='products/')
         color = models.CharField(max_length=255)
         size = models.CharField(max_length=255)
         price = models.FloatField()
         brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
         categoey = models.ForeignKey(category, on_delete=models.CASCADE)
         description = models.TextField(blank=True , null=True)

         def __str__(self):
              return self.title
