# Generated by Django 3.0.5 on 2020-04-16 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('ISBN', models.TextField()),
                ('book_rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('location', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
