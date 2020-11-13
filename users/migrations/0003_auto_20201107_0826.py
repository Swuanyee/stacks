# Generated by Django 3.1.1 on 2020-11-07 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.CharField(choices=[('Sec 1', 'sec_1'), ('Sec 2', 'sec_2'), ('Sec 3', 'sec_3'), ('Sec 4', 'sec_4'), ('J1', 'j1'), ('J2', 'j2'), ('Public', 'public'), ('Teacher', 'teacher')], default='Public', max_length=100),
        ),
    ]
