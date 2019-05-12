from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label=u"Имя пользователя")
    email = forms.EmailField(label=u"Email", required=True)
    password = forms.CharField(label=u"Пароль", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label=u"Подтвердите пароль", widget=forms.PasswordInput)

    def is_valid(self):
        valid = super(RegisterForm, self).is_valid()
        if self.cleaned_data['password'] != self.cleaned_data['password_confirm']:
            self.add_error("password_confirm", u"Пароли не совпадают")
            return False
        return valid
