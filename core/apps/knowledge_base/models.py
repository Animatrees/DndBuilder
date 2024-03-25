from django.db import models


class Characteristic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Characteristic'
        verbose_name_plural = 'Characteristics'
        db_table = 'characteristics'
        ordering = ['title']
