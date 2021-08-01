# Generated by Django 3.2.4 on 2021-07-06 19:28

import articles.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('title_uk', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_uk', models.TextField(null=True, verbose_name='Description')),
                ('description_ru', models.TextField(null=True, verbose_name='Description')),
                ('published', models.BooleanField(default=True, verbose_name='If published')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Brouser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('title_uk', models.CharField(max_length=20, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=20, null=True, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Brouser',
                'verbose_name_plural': 'Brousers',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('title_uk', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=50, null=True, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='Icon')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_uk', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('published', models.BooleanField(default=True, verbose_name='If published')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.category', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BrouserSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('support_version', models.CharField(max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('atricle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('brouser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.brouser')),
            ],
            options={
                'verbose_name': 'Brouser Support',
                'verbose_name_plural': 'Brousers Supports',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ArticleScript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script_file', models.FileField(upload_to=articles.utils.generate_upload_script_path, verbose_name='Script file')),
                ('script_type', models.CharField(choices=[('CSS', 'CSS'), ('JS', 'JavaScript')], max_length=3, verbose_name='Script type')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('atricle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_file', models.ImageField(upload_to=articles.utils.generate_upload_image_path, verbose_name='Image file')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('atricle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article', verbose_name='Article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.category', verbose_name='Category'),
        ),
    ]
