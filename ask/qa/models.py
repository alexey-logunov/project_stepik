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
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set', null=True)

    def get_absolute_url(self):
        return reverse('question', kwargs={'question_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
