# Generated by Django 5.1.3 on 2024-11-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_post2_remove_post_description_remove_post_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productinfotype',
            name='value',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
