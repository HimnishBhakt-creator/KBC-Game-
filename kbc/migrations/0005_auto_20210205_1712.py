# Generated by Django 3.0.6 on 2021-02-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kbc', '0004_auto_20210205_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='questions',
            field=models.CharField(max_length=250),
        ),
    ]
