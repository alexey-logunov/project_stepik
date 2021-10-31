from django import forms
from .models import Answer, Question
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'question')
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5}),
            'question': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

    def clean_text(self):
        text = self.cleaned_data['text']
        # if not is_ethic(text):
        #     raise forms.ValidationError(u'Сообщение не корректно', code=12)
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


# class AnswerForm(forms.Form):
#     text = forms.CharField(label='Ответ',
#                            required=False,
#                            widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}, )
#                            )
#     question = forms.ModelChoiceField(empty_label='Выберите вопрос, на который хотите ответить',
#                                       queryset=Question.objects.all(),
#                                       widget=forms.Select(attrs={'class': 'form-control'}, )
#                                       )
#
#     # def __init__(self, user, *args, **kwargs):
#     #     self._user = user
#     #     super(AnswerForm, self).__init__(*args, **kwargs)
#
#     # def clean(self):
#     #     if self._user.is_banned:
#     #         raise ValidationError(u'Доступ ограничен')
#
#     # def save(self):
#     #     self.cleaned_data['author'] = self._user
#     #     return Answer.objects.create(**self.cleaned_data)
#
#     def clean_text(self):
#         text = self.cleaned_data['text']
#         # if not is_ethic(answer):
#         #     raise forms.ValidationError(u'Сообщение не корректно', code=12)
#         return text
#
#     def save(self):
#         answer = Answer(**self.cleaned_data)
#         answer.save()
#         return answer


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
        }),
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )
        user.save()
        auth = authenticate(**self.cleaned_data)
        return auth


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control mt-2",
            'id': "inputPassword",
        })
    )
