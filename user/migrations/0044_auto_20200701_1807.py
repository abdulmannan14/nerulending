# Generated by Django 3.0.5 on 2020-07-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0043_auto_20200627_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Email Address'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='fax_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Fax Number'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='toll_free_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Toll Free Number'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Website'),
        ),
    ]