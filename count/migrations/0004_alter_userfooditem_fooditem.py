# Generated by Django 3.2.8 on 2021-12-31 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count', '0003_auto_20211125_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfooditem',
            name='fooditem',
            field=models.ManyToManyField(to='count.Fooditem'),
        ),
    ]