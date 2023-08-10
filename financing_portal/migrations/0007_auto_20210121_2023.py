# Generated by Django 3.1.4 on 2021-01-21 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('financing_portal', '0006_auto_20210121_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='recurring',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productpurchasedmodel',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='financing_portal.product'),
            preserve_default=False,
        ),
    ]