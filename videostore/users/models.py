from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

CHOICE = (('male', 'Мужской'), ('female', 'Женский'))
CHOICE_TYPE_ACCOUNT = (('full', 'Полный пакет'), ('free', 'Бесплатный пакет'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name='Фото профиля',
        default='default.png',
        upload_to='user_images'
        )
    male = models.CharField(
        verbose_name='Пол',
        max_length=100,
        choices=CHOICE,
        default='male'
        )
    email_send = models.BooleanField(
        verbose_name='Рассылка',
        default=True
    )
    acount_type = models.CharField(
        verbose_name='Тип аккаунта',
        max_length=100,
        choices=CHOICE_TYPE_ACCOUNT,
        default='free'
    )
    
    def save(self, *args, **kwargs):
        super().save()
        image = Image.open(self.image.path)
        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.image.path)
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль { self.user.username }'