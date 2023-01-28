from rest_framework import serializers
from .models import Question
from django.utils import timezone
from rest_framework.fields import empty


class QuestionManage():
    def create_question(self, request):
        question_serializer = QuestionSerializer()   
        question_serializer.title = request.POST['title']
        question_serializer.content=request.POST['content']
        question_serializer.create_date=timezone.now()
        question_serializer.author_id=request.user.id      

        return question_serializer

class QuestionSerializer(serializers.ModelSerializer):
    
    author_id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()

    def create(self,validated_data):
        question = Question.objects.create(
            title=self.validated_data['title'],
            content=self.validated_data['content'], 
            author_id=self.validated_data['author_id'])
        return question

    # def save(self):
    #     print(self.validated_data)

    class Meta:
        model = Question
        # fields = '__all__'
        fields = ['author_id','title','content']