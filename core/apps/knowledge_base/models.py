from django.db import models


class Characteristic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Characteristic'
        verbose_name_plural = 'Characteristics'
        db_table = 'characteristics'
        ordering = ['pk']

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    characteristic = models.ForeignKey(Characteristic, on_delete=models.CASCADE, related_name='skills')

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        db_table = 'skills'
        ordering = ['title']

    def __str__(self):
        return self.title


class Language(models.Model):

    LANGUAGE_TYPES = (
        ('ethnic', 'Этнические языки'),
        ('exotic', 'Экзотические языки'),
        ('secret', 'Тайные языки'),
    )

    SCRIPT_TYPES = (
        ('giants', 'Великанья'),
        ('dwarven', 'Дварфская'),
        ('common', 'Общая'),
        ('elvish', 'Эльфийская'),
        ('infernal', 'Инфернальная'),
        ('draconic', 'Драконья'),
        ('celestial', 'Небесная'),
        ('-', 'Отсутствует')
    )

    title = models.CharField(max_length=100)
    speakers = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=LANGUAGE_TYPES, null=True)
    script = models.CharField(max_length=50, choices=SCRIPT_TYPES, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        db_table = 'languages'
        ordering = ['title']

    def __str__(self):
        return self.title
