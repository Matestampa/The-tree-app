# Generated by Django 3.2.7 on 2021-11-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantar', '0005_alter_plantados_ubi_coord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantados',
            name='en_cuidado',
            field=models.BooleanField(default=False),
        ),
    ]