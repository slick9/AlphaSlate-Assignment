# Generated by Django 3.1.2 on 2020-10-03 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20201003_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='res_time',
            field=models.CharField(default='23:21:38.929078', max_length=1000),
        ),
    ]