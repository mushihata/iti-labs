# Generated by Django 3.1.4 on 2021-03-14 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long', models.CharField(max_length=50)),
                ('short', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('production_year', models.IntegerField(default=2021)),
                ('categories', models.ManyToManyField(related_name='movies', to='netflix.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='netflix/movies/videos')),
                ('resolutin', models.CharField(max_length=10)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netflix.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='netflix/movies/images')),
                ('resolutin', models.CharField(max_length=10)),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='netflix.movie')),
            ],
        ),
    ]
