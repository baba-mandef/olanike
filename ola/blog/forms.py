from django import forms
from ola.blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'author_name', 'author_pic')
        labels = {
            'body': 'Your comment',
            'author_name': 'Your name',
            'author_pic' : 'Your Picture'
        }
