from django.forms import Textarea
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "post_picture",
            "text",
        ]
        widgets = {
            'text' : Textarea(attrs={'rows' : 3, 'style' : 'width:50%', 'placeholder' : 'What\'s up?'}),
        }
        labels = {
            'text' : "",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "comment_picture",
            "text",
        ]
        widgets = {
            'text' : Textarea(attrs={'rows' : 3, 'style' : 'width:40%', 'placeholder' : 'Leave a comment'}),
        }
        labels = {
            'text' : "",
        }
