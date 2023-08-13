from django.db import models


class Point(models.Model):
    name = models.CharField(max_length=20)
    use_of_info_li = models.TextField(null=True, blank=True)
    info_share_li = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Point'
        verbose_name_plural = 'Points'


class Privacy(models.Model):
    use_of_info_li = models.ManyToManyField('Point', related_name='use_of_info_points')
    info_share_li = models.ManyToManyField('Point', related_name='info_share_points')
    choices_rights = models.TextField(max_length=550)
    personal_data = models. TextField(max_length=550)
    policy_update = models.TextField(max_length=550)
    info_context = models.TextField(max_length=550)
    third_party = models.TextField(max_length=550)
    use_of_info = models.TextField(max_length=550)
    usage_data = models. TextField(max_length=550)
    info_share = models.TextField(max_length=550)
    cookies = models. TextField(max_length=550)
    security = models.TextField(max_length=550)
    name = models.CharField(max_length=20)
    date = models.DateField(auto_now=True)
    introduction = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'new_hightech'
        verbose_name = 'Private'
        verbose_name_plural = 'Privacy'
