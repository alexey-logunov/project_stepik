from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Question, Answer
from django.core.paginator import Paginator, EmptyPage
from .forms import AnswerForm, AskForm
from django.contrib.auth.decorators import login_required


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
            page_number = int(request.GET.get('page', 1))
        except ValueError:
            raise Http404
        paginator = Paginator(questions, limit)
        try:
            page = paginator.page(page_number)
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
        form = AnswerForm()
        return render(request, 'qa/question_details.html', {
            'question_details': question_details,
            'answers': answers,
            'form': form,
        })

    def post(self, request, question_id, *args, **kwargs):
        form = AnswerForm(request.POST)
        if form.is_valid():
            text = request.POST['text']
            question_details = get_object_or_404(Question, pk=question_id)
            author = self.request.user
            # print(form.cleaned_data)
            answer = Answer.objects.create(question_details=question_details, author=author, text=text)
            # answer = Answer.objects.create(**form.cleaned_data)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            # return redirect(answer)
            # answer = form.save()
            # url = answer.get_url()
            # return HttpResponseRedirect(url)
        return render(request, 'qa/question_details.html', {
            'form': form,
        })

# @login_required
# def answer_add(request):
#     if request.method == "POST":
#         # form = AnswerForm(request.user, request.POST)
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             answer = Answer.objects.create(**form.cleaned_data)
#             return redirect(answer)
#             # answer = form.save()
#             # url = answer.get_url()
#             # return HttpResponseRedirect(url)
#     else:
#         form = AnswerForm()
#     return render(request, 'qa/answer_add.html', {
#         'form': form
#     })


@login_required
def question_add(request):
    if request.method == "POST":
        # form = AskForm(request.user, request.POST)
        form = AskForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            question = Question.objects.create(**form.cleaned_data)
            # question = form.save()
            return redirect(question)
            # question = form.save()
            # url = question.get_url()
            # return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/question_add.html', {
        'form': form
    })
