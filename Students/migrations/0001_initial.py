# Generated by Django 2.1 on 2018-09-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registertable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.IntegerField(max_length=120)),
                ('name', models.CharField(max_length=300)),
                ('department', models.CharField(max_length=300)),
                ('year', models.IntegerField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('password', models.CharField(max_length=300)),
                ('reg_type', models.CharField(max_length=300)),
            ],
        ),
    ]
