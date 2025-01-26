from django import forms
from .models import Course, Comment

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['slug', 'title', 'description', 'image']
        labels = {
            'slug': 'Название URL',
            'title': 'Название курса',
            'description': 'Описание курса',
            'image': 'Изображение курса',
        }
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название URL'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название курса'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание курса'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Изображение курса'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text_comment']
        labels = {
            'text_comment': 'Сообщение*',
        }
        widgets = {
            'text_comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Напишите комментарий'}),
        }