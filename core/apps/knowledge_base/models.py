from django.db import models


class Characteristic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Characteristic'
        verbose_name_plural = 'Characteristics'
        db_table = 'characteristics'
        ordering = ['pk']

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, related_name='skills')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        db_table = 'skills'
        ordering = ['title']

    def __str__(self):
        return self.title
