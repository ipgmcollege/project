# Generated by Django 2.0.2 on 2018-08-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=50)),
                ('issued', models.BooleanField()),
                ('copies', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chem_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=50)),
                ('issued', models.BooleanField()),
                ('copies', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Elec_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=50)),
                ('issued', models.BooleanField()),
                ('copies', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mech_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=50)),
                ('issued', models.BooleanField()),
                ('copies', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Lib_Model',
            new_name='Tech_Model',
        ),
    ]
