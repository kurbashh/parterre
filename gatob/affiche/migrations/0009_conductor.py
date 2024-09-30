# Generated by Django 4.2.13 on 2024-05-22 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('affiche', '0008_alter_performance_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conductor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('performance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='affiche.performance')),
            ],
            options={
                'verbose_name_plural': 'Conductors',
            },
        ),
    ]
