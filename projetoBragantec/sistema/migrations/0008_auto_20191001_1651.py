# Generated by Django 2.2.5 on 2019-10-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0007_auto_20191001_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='curso',
            field=models.CharField(default=None, max_length=100, verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='idade',
            field=models.IntegerField(default=None, verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='instituicao',
            field=models.CharField(default=None, max_length=100, verbose_name='Instituição'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(default=None, max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='serie',
            field=models.CharField(default=None, max_length=100, verbose_name='Série'),
        ),
    ]