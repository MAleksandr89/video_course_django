# Generated by Django 4.2.16 on 2024-10-28 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default.png', upload_to='courses_images/', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='Уникальное название урока')),
                ('title', models.CharField(max_length=120, verbose_name='Название урока')),
                ('description', models.TextField(verbose_name='Описание урока')),
                ('number', models.IntegerField(verbose_name='Номер текущего урока')),
                ('video_url', models.URLField(blank=True, max_length=100, verbose_name='Ссылка на видео')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Какой курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
