from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Choose category'
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Add Post',
                'title',
                'text',
                'photo',
                'category',
                'is_published',
                HTML('<br><br>'),
                Submit('register', 'Register'),
            ))

    # class Meta:
    #     model = Post
    #     fields = ['title', 'slug', 'text', 'photo', 'category', 'is_published']
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class': 'form-input'}),
    #         'text': forms.Textarea(attrs={'cols': 60, 'rows': 12}),
    #     }


class RegisterUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Register',
                'username',
                'password1',
                'password2',
                HTML('<br><br>'),
                Submit('register', 'Register'),
            ))


    # class Meta:
    #     username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #     # email = forms.EmailField(label='Email address', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    #     password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    #     password2 = forms.CharField(label='Repeat Password',
    #                                 widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset(
                'Login',
                'username',
                'password',
            HTML('<br><br>'),
            Submit('login', 'Login'),
        ))

    # username = forms.CharField(label='Login', widget=forms.TextInput())
    # password = forms.CharField(label='Password', widget=forms.PasswordInput())
