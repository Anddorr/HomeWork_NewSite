from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    search_product = forms.CharField(max_length=256)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.Form):
    comment = forms.CharField(label="Write comment", widget=forms.Textarea)


class ArticleForm(forms.Form):
    article_name = forms.CharField(label="Write article name")
    article_info = forms.CharField(label='Write article info', widget=forms.Textarea)