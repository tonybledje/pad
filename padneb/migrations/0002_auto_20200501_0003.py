# Generated by Django 2.2.12 on 2020-05-01 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('padneb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='Amount',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='contribution',
            old_name='Contribution_Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='guardian',
            old_name='Middle_Initial',
            new_name='middle_initial',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='Middle_Initial',
            new_name='middle_initial',
        ),
    ]
