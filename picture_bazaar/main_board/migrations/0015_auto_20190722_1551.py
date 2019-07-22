# Generated by Django 2.2.3 on 2019-07-22 15:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0014_auto_20190722_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
