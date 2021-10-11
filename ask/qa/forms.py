from django import forms
from .models import Answer, Question


# class AskForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название вопроса',
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))
#     text = forms.CharField(label='Описание вопроса', required=False, widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'rows': 5,
#     }))

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

    # def __init__(self, user, *args, **kwargs):
    #     self._user = user
    #     super(AskForm, self).__init__(*args, **kwargs)

    def clean_text(self):
        text = self.cleaned_data['text']
        # if not is_ethic(text):
        #     raise forms.ValidationError(u'Сообщение не корректно', code=12)
        return f'{text}\nThank you for your attention!'

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


# class AnswerForm(forms.ModelForm):
#     class Meta:
#         model = Answer
#         fields = ('text', 'question')
#         widgets = {
#             'text': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 5}),
#             'question': forms.Select(attrs={
#                 'class': 'form-control',
#             }),
#         }


class AnswerForm(forms.Form):
    text = forms.CharField(label='Ответ',
                           required=False,
                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}, )
                           )
    question = forms.ModelChoiceField(empty_label='Выберите вопрос, на который хотите ответить',
                                      queryset=Question.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}, )
                                      )

    # def __init__(self, user, *args, **kwargs):
    #     self._user = user
    #     super(AnswerForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     if self._user.is_banned:
    #         raise ValidationError(u'Доступ ограничен')

    # def save(self):
    #     self.cleaned_data['author'] = self._user
    #     return Answer.objects.create(**self.cleaned_data)

    def clean(self):
        answer = self.cleaned_data['text']
        # if not is_ethic(answer):
        #     raise forms.ValidationError(u'Сообщение не корректно', code=12)
        return f'{answer}\nThank you for your attention!'

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
