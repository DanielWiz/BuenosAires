# Generated by Django 2.0.13 on 2019-07-08 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aires_acondicionados', '0002_remove_servicios_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100)),
                ('Imagen', models.ImageField(upload_to='')),
                ('Stock', models.IntegerField()),
            ],
        ),
    ]
