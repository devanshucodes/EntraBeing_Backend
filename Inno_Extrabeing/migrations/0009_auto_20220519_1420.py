# Generated by Django 2.0 on 2022-05-19 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inno_Extrabeing', '0008_user_security'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_security',
            name='Token',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
