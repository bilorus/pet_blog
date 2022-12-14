from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
                # 'slug',
                'text',
                HTML('<br>'),
                'photo',
                HTML('<br>'),
                'category',
                HTML('<br>'),
                'is_published',
                HTML('<br><br>'),
                Submit('submit', 'Post'),
            ))

    class Meta:
        model = Post
        fields = ['title', 'text', 'photo', 'category', 'is_published']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 3, 'class': "form-control", 'placeholder': "Join the discussion and leave a comment!"})
        }


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
