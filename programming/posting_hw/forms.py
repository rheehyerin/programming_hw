from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from .models import Post, Comment, Tag

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'tag_set', 'created_at']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message']
        error_messages = {
            NON_FIELD_ERRORS:{
                'min_length_error' :"%(title)s's %(field_labels)s are not validated.",
            }
        }
