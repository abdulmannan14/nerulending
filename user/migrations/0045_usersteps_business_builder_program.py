# Generated by Django 3.0.5 on 2020-07-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0044_auto_20200701_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersteps',
            name='business_builder_program',
            field=models.IntegerField(choices=[(1, 'Not ordered'), (2, 'In progress'), (3, 'Done')], default=1,
                                      null=True, verbose_name='Toll free number'),
        ),
    ]