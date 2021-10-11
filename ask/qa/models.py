from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255, blank=True, verbose_name='Название вопроса')
    text = models.TextField(blank=True, verbose_name='Описание вопроса')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации вопроса')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг вопроса')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Автор вопроса')
    likes = models.ManyToManyField(User, related_name='likes_set', verbose_name='Количество лайков вопроса')

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField(blank=True, verbose_name='Текст ответа')
    added_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answers', verbose_name='Вопрос')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_name', verbose_name='Автор ответа')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['-added_at']
