from django.db import models
from fontawesome_5.fields import IconField
from PIL import Image
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=35, default='New')
    img = models.ImageField(upload_to='ampmedia/img')
    projectName = models.CharField(max_length=20)
    context = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            pic = Image.open(self.img.path)
            if pic.height > 450 or pic.width > 550:
                new_pic = (550, 450)
                pic.thumbnail(new_pic)
                pic.save(self.img.path)

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'project'
        verbose_name_plural = 'projects'
