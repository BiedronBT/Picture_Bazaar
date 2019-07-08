# Generated by Django 2.2.3 on 2019-07-08 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_board', '0009_auto_20190707_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='height',
            field=models.IntegerField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(height_field='height', upload_to='images', width_field='width'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='tags',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='picture',
            name='title',
            field=models.CharField(max_length=63),
        ),
        migrations.AlterField(
            model_name='picture',
            name='width',
            field=models.IntegerField(auto_created=True),
        ),
    ]
