# Generated by Django 3.1.6 on 2023-02-02 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='decsription',
            new_name='description',
        ),
    ]
