# Generated by Django 4.0.4 on 2022-05-26 18:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Category title')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Category title')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Category title')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Category URL')),
            ],
            options={
                'verbose_name': ('Category',),
                'verbose_name_plural': "Category's",
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d', verbose_name='Post image')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Post video')),
                ('title', models.CharField(max_length=100, verbose_name='Post name')),
                ('title_ru', models.CharField(max_length=100, null=True, verbose_name='Post name')),
                ('title_en', models.CharField(max_length=100, null=True, verbose_name='Post name')),
                ('text', models.TextField(max_length=360, verbose_name='Text in post list')),
                ('text_ru', models.TextField(max_length=360, null=True, verbose_name='Text in post list')),
                ('text_en', models.TextField(max_length=360, null=True, verbose_name='Text in post list')),
                ('description', models.CharField(max_length=2000, verbose_name='Full post text')),
                ('description_ru', models.CharField(max_length=2000, null=True, verbose_name='Full post text')),
                ('description_en', models.CharField(max_length=2000, null=True, verbose_name='Full post text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Post creation date')),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10, verbose_name='Visible status')),
                ('is_new', models.BooleanField(default=False, verbose_name='New post indicator')),
                ('slug', models.SlugField(max_length=250, unique_for_date='created', verbose_name='Post URL')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Post author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post', to='blog.category', verbose_name='Post category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': ('Post',),
                'verbose_name_plural': 'Posts',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='comment', verbose_name='User image')),
                ('author', models.CharField(max_length=50, verbose_name='Authors name')),
                ('text', models.TextField(max_length=500, verbose_name='Comment text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Comment creation date')),
                ('email', models.EmailField(max_length=100, verbose_name='User email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Comment visibility')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='blog.comment', verbose_name='Parent comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.post', verbose_name='Relevant post')),
            ],
            options={
                'verbose_name': ('Comment',),
                'verbose_name_plural': 'Comments',
                'ordering': ('created',),
            },
        ),
    ]
