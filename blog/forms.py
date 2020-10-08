from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'author_name',)
        labels = {
            'body': 'Your comment',
            'author_name': 'Your name',

        }
