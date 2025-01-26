from django.views.generic import ListView, DetailView, CreateView
from .models import Course, Lesson, Comment
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import CourseForm, CommentForm
from django.contrib import messages

class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница сайта'
        return context
    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        context['title'] = course
        context['lessons'] = Lesson.objects.filter(course = course).order_by('number')
        return context
    
class LessonDetailView(DetailView):
    model = Course
    form_class = CommentForm
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'course'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.author = self.request.user
            form.instance.lesson = Lesson.objects.filter(slug = self.kwargs['lessons_slug']).first()
            form.save()
            messages.success(request, 'Комментарий добавлен')
            return self.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = Lesson.objects.filter(slug = self.kwargs['lessons_slug']).first()
        comments = Comment.objects.filter(lesson = lesson)

        context['title'] = lesson
        context['lesson'] = lesson
        context['comments'] = comments
        context['form'] = self.form_class
        return context
    
def TarifView(request):
    return render(request, 'courses/tarif.html', {'title': 'Тарифы на сайте'})

class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/add_course.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.success(self.request, 'Курс успешно добавлен')
        return super(CreateCourseView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление нового курса'
        return context