# Generated by Django 4.2.5 on 2023-10-06 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_rename_content_article_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='discription',
            new_name='description',
        ),
    ]
