# Generated by Django 4.2.3 on 2023-07-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snack',
            options={'ordering': ['-pk']},
        ),
        migrations.AlterField(
            model_name='snack',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
