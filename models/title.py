from django.db import models


class TitleModel(models.Model):
    favicon = models.ImageField(upload_to='ampmedia/favicon')
    secondSlideSubTitle = models.CharField(max_length=50)
    firstSlideSubTitle = models.CharField(max_length=50)
    testimonySubTitle = models.CharField(max_length=50)
    secondSlideTitle = models.CharField(max_length=70)
    firstSlideTitle = models.CharField(max_length=70)
    contactSubTitle = models.CharField(max_length=50)
    projectSubTitle = models.CharField(max_length=50)
    serviceSubTitle = models.CharField(max_length=50)
    testimonyTitle = models.CharField(max_length=70)
    footerSubTitle = models.CharField(max_length=50)
    aboutSubTitle = models.CharField(max_length=50)
    staffSubTitle = models.CharField(max_length=50)
    studentTitle = models.CharField(max_length=70)
    blogSubTitle = models.CharField(max_length=50)
    contactTitle = models.CharField(max_length=70)
    projectTitle = models.CharField(max_length=70)
    serviceTitle = models.CharField(max_length=70)
    privacyTitle = models.CharField(max_length=70)
    searchTitle = models.CharField(max_length=50)
    footerTitle = models.CharField(max_length=70)
    staffTitle = models.CharField(max_length=70)
    aboutTitle = models.CharField(max_length=70)
    termsTitle = models.CharField(max_length=70)
    pageTitle = models.CharField(max_length=50)
    blogTitle = models.CharField(max_length=70)
    faqTitle = models.CharField(max_length=70)

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Title'
