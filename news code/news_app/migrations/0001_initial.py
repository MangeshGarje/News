# Generated by Django 3.1.5 on 2021-01-24 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('short_desc', models.CharField(max_length=600)),
                ('published', models.CharField(max_length=10)),
                ('category', models.ManyToManyField(to='news_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13)),
                ('category', models.ManyToManyField(to='news_app.Category')),
                ('publisher', models.ManyToManyField(to='news_app.Publisher')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='usercat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news_app.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='newsDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10000)),
                ('pictures', models.ImageField(null=True, upload_to='')),
                ('news', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news_app.news')),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news_app.publisher'),
        ),
    ]