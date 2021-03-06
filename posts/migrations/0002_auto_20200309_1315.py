# Generated by Django 2.2.10 on 2020-03-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Dj', 'Django'), ('R', 'Ruby')], default=None, max_length=3),
        ),
        migrations.AddField(
            model_name='post',
            name='custom_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='post',
            name='last_published',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]
