from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from .models import Post, Comment, Tag

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'photo', 'title', 'content', 'tag_set', 'created_at']


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author','photo', 'message']
        error_messages = {
            NON_FIELD_ERRORS:{
                'min_length_error' :"%(title)s's %(field_labels)s are not validated.",
            }
        }

class CommentForm(forms.Form):
    author = forms.CharField(max_length=20)
    photo = forms.ImageField()
    message = forms.CharField(widget=forms.Textarea, max_length=100)
    def save(self, commit=True):
        comment = Comment(author=self.cleaned_data['author'], photo=self.cleaned_data['photo'], message=self.cleaned_data['message'])
       # comment.post_id = post_pk
        if commit:
            comment.save()
        return comment