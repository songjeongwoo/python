# Generated by Django 3.2.5 on 2022-02-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_auto_20220209_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
