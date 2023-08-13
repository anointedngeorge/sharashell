from django.db import models
from fontawesome_5.fields import IconField
# Create your models here.


class Service(models.Model):

    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    content = models.TextField(max_length=120)
    fullContent = models.TextField()
    slug = models.SlugField(default='', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'service'
        verbose_name_plural = 'services'
