from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        db_table = 'sections'
        ordering = ['title']

    def __str__(self):
        return self.title


class Source(models.Model):
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Source'
        verbose_name_plural = 'Sources'
        db_table = 'sources'
        ordering = ['title']

    def __str__(self):
        return self.short_title


class Characteristic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, related_name='characteristics')
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, related_name='characteristics')

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
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, related_name='skills')
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, related_name='skills')

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
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, related_name='languages')
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING, related_name='languages')

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        db_table = 'languages'
        ordering = ['title']

    def __str__(self):
        return self.title


class Die(models.Model):
    title = models.CharField(max_length=10)
    modifier = models.SmallIntegerField()
    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name='dice')
    source = models.ForeignKey(Source, on_delete=models.PROTECT, related_name='dice')

    class Meta:
        verbose_name = 'Die'
        verbose_name_plural = 'Dice'
        db_table = 'dice'
        ordering = ['modifier']

    def __str__(self):
        return self.title


class Coin(models.Model):
    title = models.CharField(max_length=20)
    short_title = models.CharField(max_length=5)
    rate = models.DecimalField(max_digits=4, decimal_places=1)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, related_name='coins')
    source = models.ForeignKey(Source, on_delete=models.PROTECT, related_name='coins')

    class Meta:
        verbose_name = 'Coin'
        verbose_name_plural = 'Coins'
        db_table = 'coins'
        ordering = ['rate']

    def __str__(self):
        return self.title

