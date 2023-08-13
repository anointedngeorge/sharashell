from django.db import models

 
class TermsAndCondition(models.Model):
    name = models.CharField(max_length=20)
    introduction = models.TextField(max_length=550)
    use_of_site = models.TextField(max_length=550)
    intel_property = models.TextField(max_length=550)
    user_content = models.TextField(max_length=550)
    liability = models.TextField(max_length=550)
    indemnification = models.TextField(max_length=550)
    modification = models.TextField(max_length=550)
    law = models.TextField(max_length=550)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Term'
        verbose_name_plural = 'Our Terms'