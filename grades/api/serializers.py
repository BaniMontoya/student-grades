from rest_framework.serializers import ModelSerializer, Serializer
from .models import Question, Student
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        depth = 2
        fields = '__all__'

from .models import StudentAnswer


class StudentAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAnswer
        fields = ['id', 'question', 'answer_text', 'student']
        read_only_fields = ['id', 'student']

    def validate_question(self, value):
        try:
            question = Question.objects.get(pk=value.pk)
        except Question.DoesNotExist:
            raise serializers.ValidationError("Question does not exist.")
        return question

        
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
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
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
