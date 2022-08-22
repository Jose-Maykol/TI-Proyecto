# Generated by Django 4.0.6 on 2022-07-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8, verbose_name='DNI')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del tecnico')),
                ('address', models.CharField(max_length=50, verbose_name='Direccion')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('phone_number', models.CharField(max_length=9, verbose_name='Numero de telefono')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('service_hours', models.CharField(max_length=50, verbose_name='Horario de servicio')),
            ],
            options={
                'verbose_name': 'Tecnico',
                'verbose_name_plural': 'Tecnico',
            },
        ),
    ]
