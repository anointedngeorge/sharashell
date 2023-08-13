from django.db import models
from fontawesome_5.fields import IconField
from PIL import Image
# Create your models here.


class Slider(models.Model):
    name = models.CharField(max_length=35, default='New')
    img2 = models.ImageField(upload_to='ampmedia/img')
    img = models.ImageField(upload_to='ampmedia/img')
    subTitle2 = models.CharField(max_length=35)
    title2 = models.CharField(max_length=70)
    title = models.CharField(max_length=70)
    description2 = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name


    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'


class Fact(models.Model):
    numb = models.IntegerField()
    content = models.CharField(max_length=100)

    class Meta:
        app_label = 'new_hightech'
