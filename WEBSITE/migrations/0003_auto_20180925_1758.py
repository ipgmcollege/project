# Generated by Django 2.1 on 2018-09-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0002_auto_20180925_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registertable',
            name='department',
        ),
        migrations.RemoveField(
            model_name='registertable',
            name='year',
        ),
        migrations.AlterField(
            model_name='registertable',
            name='email',
            field=models.EmailField(max_length=120),
        ),
        migrations.AlterField(
            model_name='registertable',
            name='uname',
            field=models.IntegerField(max_length=120),
        ),
    ]
