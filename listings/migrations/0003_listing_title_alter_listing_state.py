# Generated by Django 4.0.6 on 2022-07-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_dcscription_listing_decscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(default='AL', max_length=100),
        ),
    ]
