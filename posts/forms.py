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
            'video',
        )

        title = forms.CharField()
        content = forms.CharField()
        image = forms.ImageField(required=False)
        video = forms.FileField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get('video')
        image = cleaned_data.get('image')

        if not video and not image:

            raise forms.ValidationError('Необходимо загрузить хотя бы одно фото или видео.')

        if video:
            cleaned_data['is_video'] = True
        else:
            cleaned_data['is_video'] = False



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

