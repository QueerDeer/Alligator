from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label=u"Имя пользователя", required=True)
    email = forms.EmailField(label=u"Email", required=True)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput, required=True)
    re_password = forms.CharField(label=u"Подтвердите пароль", widget=forms.PasswordInput, required=True)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()

        username = self.cleaned_data['username']
        email = self.cleaned_data['email']

        if User.objects.filter(username=username).exists():
            self.add_error('username', u'Username "%s" is already in use.' % username)
            valid = False

        if User.objects.filter(email=email).exists():
            self.add_error('email', u'Email "%s" is already in use.' % email)
            valid = False

        if self.cleaned_data['password'] != self.cleaned_data['re_password']:
            self.add_error('re_password', u'Passwords does not equal')
            valid = False

        return valid
