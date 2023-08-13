from django.db import models
from fontawesome_5.fields import IconField
from PIL import Image
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=35, default='New')
    img = models.ImageField(upload_to='ampmedia/img')
    projectName = models.CharField(max_length=20)
    context = models.CharField(max_length=50)
    fullContent = models.TextField()
    slug = models.SlugField(default='', max_length=20)
    
    def __str__(self):
        return self.name

 

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'project'
        verbose_name_plural = 'projects'
