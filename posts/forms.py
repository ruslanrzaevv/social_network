from django import forms


from posts.models import Post
from posts.models import Comment


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



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

