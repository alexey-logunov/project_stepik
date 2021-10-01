from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()


class Answer(models.Model):
    user = User.objects.get_or_create(username='x', defaults={'password': 'y'})[0]
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    question = Question(title='qwe', text='qwe', author=user)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
