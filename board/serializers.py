from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.ModelSerializer):
    
    author_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()

    def create(self,validated_data):
        question = Question.objects.create(
            title=validated_data['title'],
            content=validated_data['content'], 
            author_id=validated_data['author_id'])
        return question

    class Meta:
        model = Question
        # fields = '__all__'
        fields = ['id','author_id','title','content']


class AnswerSerializer(serializers.ModelSerializer):

    author_id = serializers.IntegerField()
    question_id = serializers.IntegerField()
    content = serializers.CharField()

    def create(self,validated_data):
        answer = Answer.objects.create(
            author_id=validated_data['author_id'],
            question_id=validated_data['question_id'],
            content=validated_data['content'])
        return answer

    class Meta:
        model = Answer
        # fields = '__all__'
        fields = ['author_id','question_id','content']