# Generated by Django 5.0.2 on 2024-02-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyns', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pyn',
            name='tags',
            field=models.ManyToManyField(blank=True, to='pyns.tag'),
        ),
    ]