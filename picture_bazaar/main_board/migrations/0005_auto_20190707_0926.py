# Generated by Django 2.2.3 on 2019-07-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0004_auto_20190707_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(height_field='height', upload_to='images', width_field='width'),
        ),
    ]
