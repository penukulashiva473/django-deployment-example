# Generated by Django 3.2.5 on 2021-07-15 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='protfolio_site',
            new_name='portfolio_site',
        ),
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='porfile_pic',
            new_name='profile_pic',
        ),
    ]
