# Generated by Django 3.0.5 on 2020-05-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0012_auto_20200506_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='portalgoal',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Custom portal name'),
        ),
    ]
