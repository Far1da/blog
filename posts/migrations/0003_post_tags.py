# Generated by Django 4.1.2 on 2022-11-01 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='posts.tag'),
        ),
    ]