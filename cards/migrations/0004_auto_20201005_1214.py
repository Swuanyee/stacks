# Generated by Django 3.1.1 on 2020-10-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20201005_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardsanswer',
            name='answerImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='cardsanswer',
            name='answerText',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='cardsquestion',
            name='questionImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
