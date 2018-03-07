# Generated by Django 2.0.2 on 2018-03-07 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20180306_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='photo',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='wiki_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='landmark',
            name='score',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='choice',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
