# Generated by Django 3.0.5 on 2020-04-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unset', max_length=50)),
                ('preferred_country', models.CharField(default='unset', max_length=50)),
                ('ielts_score', models.FloatField(default=0.0, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='University_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown name', max_length=50)),
                ('country', models.CharField(default='unknown country', max_length=20)),
                ('city', models.CharField(default='unknown city', max_length=20)),
                ('subject', models.CharField(default='unknown subject', max_length=50)),
                ('min_ielts', models.FloatField(default=0.0, max_length=20)),
            ],
        ),
    ]