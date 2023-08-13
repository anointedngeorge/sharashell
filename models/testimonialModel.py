from PIL import Image
from django.db import models
from fontawesome_5.fields import IconField
# Create your models here.


class Testimonial(models.Model):
    name = models.CharField(max_length=35, default='New')
    clientProfession = models.CharField(max_length=50)
    img = models.ImageField(upload_to='ampmedia/img')
    rating = models.PositiveIntegerField(default=5)
    clientName = models.CharField(max_length=20)
    feedBack = models.TextField(max_length=120)

    def __str__(self):
        return self.name


    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'testimony'
        verbose_name_plural = 'testimonial'
