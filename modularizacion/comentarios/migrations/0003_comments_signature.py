# Generated by Django 5.1.4 on 2024-12-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
            preserve_default=False,
        ),
    ]
