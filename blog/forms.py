from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'overview', 'content']


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']