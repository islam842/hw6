from django.db import models


class Kaktus(models.Model):
    title_name = models.CharField(max_length=100)
    title_url = models.URLField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title_name


