# Generated by Django 5.0.3 on 2024-04-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0008_coin_short_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='die',
            name='modifier',
            field=models.SmallIntegerField(default=4),
            preserve_default=False,
        ),
    ]
