# Generated by Django 2.2.6 on 2019-10-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20191022_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
    ]