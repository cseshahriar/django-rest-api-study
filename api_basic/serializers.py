from rest_framework import serializers
from .models import Article

# serializer
'''
class ArticleSerializer(serializers.Serializer):
    # id      = serializers.IntegerField(read_only=True)
    title   = serializers.CharField(max_length=100)
    author  = serializers.CharField(max_length=100)
    email   = serializers.CharField(max_length=100)
    date    = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title  = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email  = validated_data.get('email', instance.email)
        instance.date   = validated_data.get('date', instance.date)

        instance.save()
        return instance
'''

# Model Serializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta():
        model = Article
        fields = ['id', 'title', 'author', 'email', 'date']
