# Generated by Django 2.2.12 on 2020-05-01 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_chapter', models.CharField(max_length=3)),
                ('chapter_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('Middle_Initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('admission_date', models.DateField(verbose_name='Admitted on:')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('marital_status', models.CharField(choices=[('M', 'Married'), ('W', 'Widowed'), ('S', 'Single')], max_length=1)),
                ('in_pad_social', models.BooleanField()),
                ('date_admitted', models.DateField()),
                ('cellPhone', models.CharField(max_length=12)),
                ('homePhone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=6)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padneb.Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=35)),
                ('Middle_Initial', models.CharField(max_length=1)),
                ('last_name', models.CharField(max_length=35)),
                ('relation_to_member', models.CharField(choices=[('F', 'Father'), ('M', 'Mother'), ('S', 'Spouse'), ('O', 'Other')], max_length=1)),
                ('comments', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padneb.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contribution_Date', models.DateField()),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type', models.CharField(choices=[('MC', 'Monthly'), ('SC', 'Special'), ('AC', 'Annual Convention'), ('EY', 'End of Year Celebration')], max_length=2)),
                ('description', models.CharField(max_length=50)),
                ('comments', models.TextField()),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='padneb.Member')),
            ],
        ),
    ]