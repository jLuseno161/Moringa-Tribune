# Generated by Django 3.2.4 on 2021-06-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210628_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
    ]
