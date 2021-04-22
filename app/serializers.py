from rest_framework import serializers
from .models import Question, Comment

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'text', 'data_create', 'rating', 'author', 'tags']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text', 'data_create', 'author', 'question', 'correct_status']