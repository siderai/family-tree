# Generated by Django 4.0.4 on 2022-06-29 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='human',
            options={'verbose_name_plural': 'people'},
        ),
    ]
