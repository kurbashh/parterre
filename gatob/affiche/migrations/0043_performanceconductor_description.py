# Generated by Django 4.2.13 on 2024-06-14 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0042_rename_performer_performanceperformers_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='performanceconductor',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
