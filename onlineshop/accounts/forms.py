from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class QuizAuthenticationForm(AuthenticationForm):
    answer = forms.CharField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', ' ')
        if answer != '6':
            raise forms.ValidationError('Wrong!')

class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email', ' ')
        if email :
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('이미 등록된 이메일')
        return email

    def save(self, commit=True):
        user = super(EmailUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
