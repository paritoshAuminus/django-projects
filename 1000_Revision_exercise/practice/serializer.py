import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.datetime.now()

comment = Comment("sherry@gmail.com", "What a great comment.")


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serializer = CommentSerializer(comment)
json = JSONRenderer().render(serializer.data)
