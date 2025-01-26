from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Course(models.Model):
    slug = models.SlugField(verbose_name='Уникальное название курса', max_length=120, unique=True)
    title = models.CharField(verbose_name='Название',max_length=120)
    description = models.TextField(verbose_name='Описание курса')
    image = models.ImageField(verbose_name='Изображение',default='default.png',upload_to='courses_images/')
    is_free = models.BooleanField(verbose_name='Бесплатный урок', default=False)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    

class Lesson(models.Model):
    slug = models.SlugField(verbose_name='Уникальное название урока', max_length=120, unique=True)
    title = models.CharField(verbose_name='Название урока',max_length=120)
    description = models.TextField(verbose_name='Описание урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Какой курс')
    number = models.IntegerField(verbose_name='Номер текущего урока')
    video_url = models.URLField(verbose_name='Ссылка на видео', blank=True, max_length=100)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'slug': self.course.slug, 'lessons_slug': self.slug})
    
class Comment(models.Model):
    text_comment = models.TextField(verbose_name='Текст комментария', blank=True, )
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Какой урок')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text_comment