from django.db import models
from fontawesome_5.fields import IconField
from PIL import Image
# Create your models here.


class Blog(models.Model):
    authorImg = models.ImageField(upload_to='ampmedia/img')
    name = models.CharField(max_length=35, default='New')
    img = models.ImageField(upload_to='ampmedia/img')
    blogContent = models.TextField(max_length=120)
    blogName = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    def get_share_count(self):
        return self.share_set.count()

    def get_comment_count(self):
        return self.comment_set.count()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.img:
            pic = Image.open(self.img.path)
            if pic.height > 450 or pic.width > 600:
                new_pic = (600, 450)
                pic.thumbnail(new_pic)
                pic.save(self.img.path)

        if self.authorImg:
            pic1 = Image.open(self.authorImg.path)
            if pic1.height > 100 or pic1.width > 100:
                new_pic = (100, 100)
                pic1.thumbnail(new_pic)
                pic1.save(self.authorImg.path)

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class Share(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    sharedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'new_hightech'


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenterName = models.CharField(max_length=50)
    commentText = models.TextField()
    commentedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'new_hightech'
