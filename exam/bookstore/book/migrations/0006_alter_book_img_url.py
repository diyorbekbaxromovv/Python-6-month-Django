# Generated by Django 5.0.2 on 2024-02-07 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img_url',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
