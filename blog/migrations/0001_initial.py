# Generated by Django 3.2.5 on 2021-09-03 18:27

import ckeditor.fields
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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='İçerik')),
                ('summary', models.TextField(verbose_name='Özet')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('news_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf Ekleyin')),
                ('post_views', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar ')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
