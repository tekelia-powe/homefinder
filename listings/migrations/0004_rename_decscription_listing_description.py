# Generated by Django 4.0.6 on 2022-07-19 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_title_alter_listing_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='decscription',
            new_name='description',
        ),
    ]
