# Generated by Django 4.0.6 on 2022-07-19 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_rename_decscription_listing_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='price',
            new_name='rent',
        ),
    ]
