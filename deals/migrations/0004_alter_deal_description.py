# Generated by Django 4.1.2 on 2023-04-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0003_alter_deal_description_alter_deal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='description',
            field=models.DateTimeField(blank=True, max_length=500),
        ),
    ]
