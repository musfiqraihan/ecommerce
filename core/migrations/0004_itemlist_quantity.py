# Generated by Django 3.1.6 on 2021-02-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_itemlist_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlist',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
