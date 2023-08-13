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
    
 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            pic2 = Image.open(self.img.path)
            if pic2.height > 1080 or pic2.width > 1920:
                new_pic = (1920, 1080)
                pic2.thumbnail(new_pic)
                pic2.save(self.img.path)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

