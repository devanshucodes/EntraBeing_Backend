# Generated by Django 2.0 on 2022-05-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inno_Extrabeing', '0013_auto_20220519_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_security',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
