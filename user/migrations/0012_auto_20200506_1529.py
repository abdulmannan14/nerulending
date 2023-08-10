# Generated by Django 3.0.5 on 2020-05-06 15:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0011_auto_20200506_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='portals',
        ),
        migrations.CreateModel(
            name='PortalGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portals', models.ManyToManyField(to='user.Portal')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portal_goals',
                                              to='user.Portal')),
            ],
            options={
                'verbose_name': 'Portal Goal',
                'verbose_name_plural': 'Portal Goals',
            },
        ),
    ]
