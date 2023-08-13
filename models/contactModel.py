from django.db import models
from fontawesome_5.fields import IconField
from PIL import Image
# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=35, default='New')
    img = models.ImageField(upload_to='ampmedia/img')
    addressUrl = models.URLField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    
 

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

