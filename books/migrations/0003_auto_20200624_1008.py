# Generated by Django 2.0.3 on 2020-06-24 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200623_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowedbooks',
            name='book_isbn',
        ),
        migrations.AddField(
            model_name='borrowedbooks',
            name='id_book',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='bookid', to='books.Book'),
        ),
    ]
