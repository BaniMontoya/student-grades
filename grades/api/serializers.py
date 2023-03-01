from rest_framework.serializers import ModelSerializer, Serializer
from .models import Question, Student
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        
        # Specifies the level of depth to include when serializing Student objects
        depth = 2
        
        # Specifies which fields should be serialized for Student objects
        fields = '__all__'

from .models import StudentAnswer

class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        
        # Specifies which fields should be serialized for StudentAnswer objects
        fields = ['id', 'question', 'answer_text', 'student']
        
        # Specifies which fields should be read-only when serializing StudentAnswer objects
        read_only_fields = ['id', 'student']

    def validate_question(self, value):
        # Validates that the question associated with a StudentAnswer object exists
        try:
            question = Question.objects.get(pk=value.pk)
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question does not exist.")
        return question

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Customizes the token payload to include the user's username and email
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token

class CustomAuthTokenSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        # Validates the user's credentials and sets the user object in the attributes
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            if not user:
                msg
