from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from posts.models import Post


# class PostModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Post 
        fields = '__all__'


# def encode():
#     model = PostModel('hello','content: world')
#     model_sr = PostSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='/n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)


