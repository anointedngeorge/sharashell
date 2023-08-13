from django.db import models

class FeedBack(models.Model):
    project = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'
