from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from .models import Student, Test, Question, StudentAnswer
from .serializers import StudentAnswerSerializer


class StudentAnswerAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # create a test user
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

        # create a test exam
        self.test = Test.objects.create(
            title='Test de prueba',
            description='Este es un examen de prueba',
            start_time='2022-03-01T12:00:00Z',
            end_time='2022-03-02T12:00:00Z'
        )

        # create a test question for the exam
        self.question = Question.objects.create(
            test=self.test,
            question_text='¿Cuál es la capital de Francia?'
        )

        # create a test student
        self.student = Student.objects.create(
            user=self.user,
            address='123 Main St',
            whatsapp='555-5555'
        )

        # create a test student answer for the question
        self.student_answer = StudentAnswer.objects.create(
            question=self.question,
            student=Student.objects.get(user=self.user),
            answer_text='Paris'
        )

    def test_post_student_answer(self):
        # authenticate client with test user
        #self.client.force_authenticate(user=self.user)

        # data for student answer
        answer_data = {
            'question': self.question.pk,
            'answer_text': 'Londres'
        }
        login_data = {
            'username': 'testuser',
            'password': 'testpass'
        }
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data=login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        access_token = response.data['access']

        response = self.client.post(
            reverse('register_answer'), answer_data, HTTP_AUTHORIZATION=f'Bearer {access_token}')

        # check that a 201 CREATED response is received
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # check that the returned response matches the test student answer created earlier
        self.assertNotEqual(response.data, StudentAnswerSerializer(
            self.student_answer).data)
        self.assertEqual(response.data['answer_text'],'Londres')
