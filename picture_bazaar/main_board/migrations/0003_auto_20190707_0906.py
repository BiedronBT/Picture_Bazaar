# Generated by Django 2.2.3 on 2019-07-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0002_auto_20190707_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='height',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(height_field=models.CharField(max_length=20), upload_to='images', width_field=models.CharField(max_length=20)),
        ),
        migrations.AlterField(
            model_name='picture',
            name='width',
            field=models.CharField(max_length=20),
        ),
    ]