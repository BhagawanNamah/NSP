# Generated by Django 2.0.1 on 2018-06-13 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180612_0755'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userprofile',
            table='accounts_userprofile',
        ),
    ]
