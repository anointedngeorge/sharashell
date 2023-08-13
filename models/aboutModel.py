from django.db import models
from fontawesome_5.fields import IconField
from PIL import Image
# Create your models here.


class About(models.Model):
    name = models.CharField(max_length=35,default='New')
    img2 = models.ImageField(upload_to='ampmedia/img')
    img = models.ImageField(upload_to='ampmedia/img')
    content = models.TextField()
    
    def __str__(self):
        return self.name


    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'about'