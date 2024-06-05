# Generated by Django 4.2.13 on 2024-06-04 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_image_alter_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', related_name='genres', to='catalog.genre'),
        ),
    ]
