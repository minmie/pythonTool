# Generated by Django 3.0.6 on 2021-02-05 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterModelTable(
            name='author',
            table='AUTHOR',
        ),
        migrations.AlterModelTable(
            name='book',
            table='BOOK',
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='PUBLISHER',
        ),
    ]
