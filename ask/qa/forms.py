from django import forms
from .models import Answer, Question


class AskForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название вопроса',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label='Описание вопроса', required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
    }))

    # def __init__(self, user, *args, **kwargs):
    #     self._user = user
    #     super(AskForm, self).__init__(*args, **kwargs)

    def clean_guestion(self):
        guestion = self.cleaned_data['guestion']
        # if not is_ethic(answer):
        #     raise forms.ValidationError(u'Сообщение не корректно', code=12)
        return f'{guestion}\nThank you for your attention!'

    def save(self):
        guestion = Question(**self.cleaned_data)
        guestion.save()
        return guestion


class AnswerForm(forms.Form):
    text = forms.CharField(label='Описание вопроса',
                           required=False,
                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}, )
                           )
    question = forms.ModelChoiceField(empty_label='Выберите вопрос, на который хотите ответить',
                                      queryset=Question.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}, )
                                      )

    def __init__(self, user, *args, **kwargs):
        self._user = user
        super(AnswerForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     if self._user.is_banned:
    #         raise ValidationError(u'Доступ ограничен')

    # def save(self):
    #     self.cleaned_data['author'] = self._user
    #     return Answer.objects.create(**self.cleaned_data)

    def clean_answer(self):
        answer = self.cleaned_data['answer']
        # if not is_ethic(answer):
        #     raise forms.ValidationError(u'Сообщение не корректно', code=12)
        return f'{answer}\nThank you for your attention!'

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer
