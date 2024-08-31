from django.db import models

# Create your models here.
class immobiler_Products(models.Model):

    imagePthDir = ''
    products_type = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('terrain', 'terrain'),
        ('villa', 'villa'),
        ('riad', 'riad'),
    )

    products_location = (
        ('marrakech', 'marrakech'),
        ('fez', 'fez'),
        ('essaouira', 'essaouira'),
        ('tanger', 'tanger'),
        ('casablanca', 'casablanca'),
        ('nadour', 'nadour'),
        ('dakhla', 'dakhla'),

    )
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_address = models.CharField(max_length=100 , choices=products_location)
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_images = models.ImageField(blank=True , upload_to=imagePthDir)
    product_bathrooms = models.IntegerField(default=2)
    product_bedrooms = models.IntegerField(default=2)
    product_guests = models.IntegerField(default=2)
    product_area = models.IntegerField()
    product_type = models.CharField(max_length=10, choices=products_type)

    def ChangeImageDir(self):
        #change image upload_to using products types
        return f'{'products/'+self.product_type}'
    print(imagePthDir)

        

            

    def __str__(self):
        return self.product_name
    

    
    class Meta:
        verbose_name_plural = "Products"


