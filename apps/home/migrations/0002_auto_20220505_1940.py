# Generated by Django 3.2.11 on 2022-05-05 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(blank=True, choices=[('Tunis', 'Tunis'), ('Nabeul', 'Nabeul'), ('Sousse', 'Sousse')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='zip_code',
            field=models.CharField(default='Tunis', max_length=50),
        ),
    ]