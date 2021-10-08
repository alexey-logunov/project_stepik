from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage


def test(request, *args, **kwargs):
    return HttpResponse('OK')


class MainView(View):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.new()
        try:
            limit = int(request.GET.get('limit', 10))
        except ValueError:
            limit = 10
        if limit > 100:
            limit = 10
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            raise Http404
        paginator = Paginator(questions, limit)
        try:
            page = paginator.page(page)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        paginator.baseurl = '/?page='
        return render(request, 'qa/index.html', {
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
        })


class PopularView(View):
    def get(self, request, *args, **kwargs):
        questions = Question.objects.popular()
        try:
            limit = int(request.GET.get('limit', 10))
        except ValueError:
            limit = 10
        if limit > 100:
            limit = 10
        try:
            page = int(request.GET.get('page', 1))
        except ValueError:
            raise Http404
        paginator = Paginator(questions, limit)
        try:
            page = paginator.page(page)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        paginator.baseurl = '/popular/?page='
        return render(request, 'qa/popular.html', {
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
        })


class QuestionView(View):
    def get(self, request, question_id, *args, **kwargs):
        question_details = get_object_or_404(Question, pk=question_id)
        answers = question_details.answers.all()
        return render(request, 'qa/question_details.html', {
            'question_details': question_details,
            'answers': answers,
        })
