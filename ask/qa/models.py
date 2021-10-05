from django.db import models
from django.contrib.auth.models import User


# from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    # def new(self):
    # qs = self.get_count_answers()
    # return qs.order_by('-pk')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likes_set')

    def __str__(self):
        return self.title

    def get_url(self):
        return "/question/{}/".format(self.pk)

    # def get_url(self):
    #     return reverse('question_details', kwargs={'pk': self.pk})

    # def get_url(self):
    #     return reverse('question_details', args=[str(self.id)])

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-added_at']


class Answer(models.Model):
    text = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
