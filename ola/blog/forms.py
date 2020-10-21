from django import forms
from ola.blog.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'author_name',)
        labels = {
            'body': 'Votre commentaire',
            'author_name': 'Votre nom',

        }
