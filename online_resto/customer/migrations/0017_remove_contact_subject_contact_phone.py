# Generated by Django 4.1.2 on 2023-02-27 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_rename_siz_products_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]