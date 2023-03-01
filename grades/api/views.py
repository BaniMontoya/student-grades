from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentAnswerSerializer
from .models import Student, StudentAnswer, Question

class StudentAnswerAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    def post(self, request, format=None):
        # check if the student is authenticated
        if not request.user.is_authenticated:
            return Response({'error': 'You must be authenticated to register an answer'},
                            status=status.HTTP_401_UNAUTHORIZED)
        # get the answer data from the request data
        answer_data = request.data
        # validate the data with the serializer
        serializer = StudentAnswerSerializer(data=answer_data)
        serializer.is_valid(raise_exception=True)
        # get the question instance
        question = Question.objects.get(pk=answer_data['question'])
        # get the student instance from the authenticated user
        student = Student.objects.get(user=request.user)
        # create the answer
        answer = StudentAnswer.objects.create(
            question=question,
            student=student,
            answer_text=answer_data['answer_text']
        )
        # serialize the answer data to be returned in the response
        serialized_answer = StudentAnswerSerializer(answer)
        return Response(serialized_answer.data, status=status.HTTP_201_CREATED)
