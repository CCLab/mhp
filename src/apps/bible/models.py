from django.db import models


class Bible(models.Model):
    title = models.TextField()
    slug = models.TextField()
    cover = models.ImageField()
    pdf_file = models.FileField()


class BiblePage(models.Model):
    bible = models.ForeignKey(Bible)
    ordering = models.IntegerField()
    image_small = models.ImageField()
    image_large = models.ImageField(null=True, blank=True)
