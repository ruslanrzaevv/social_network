from django import forms
from posts.models import Post

class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        ordering = ['-at_created']

        fields = (
            'title',
            'content',
            'image',
        )

        title = forms.CharField()
        content = forms.CharField()
        image = forms.ImageField(required=False)



