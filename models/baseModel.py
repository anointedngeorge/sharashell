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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            pic = Image.open(self.img.path)
            if pic.height > 700 or pic.width > 1349:
                new_pic = (1349, 700)
                pic.thumbnail(new_pic)
                pic.save(self.img.path)

        if self.img2:
            pic1 = Image.open(self.img2.path)
            if pic1.height > 700 or pic1.width > 1349:
                new_pic = (1349, 700)
                pic1.thumbnail(new_pic)
                pic1.save(self.img2.path)

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'


class Fact(models.Model):
    numb = models.IntegerField()
    content = models.CharField(max_length=100)

    class Meta:
        app_label = 'new_hightech'
