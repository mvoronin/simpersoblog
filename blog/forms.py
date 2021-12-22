from django.forms import ModelForm, Textarea

from .models import Post


class PostModelForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'body']
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 4}),
            'body': Textarea(attrs={'id': 'post-body', 'cols': 40, 'rows': 10})
        }
