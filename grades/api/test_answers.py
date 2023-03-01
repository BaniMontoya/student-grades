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

        # crear un usuario de prueba
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

        # crear un examen de prueba
        self.test = Test.objects.create(
            title='Test de prueba',
            description='Este es un examen de prueba',
            start_time='2022-03-01T12:00:00Z',
            end_time='2022-03-02T12:00:00Z'
        )

        # crear una pregunta de prueba para el examen
        self.question = Question.objects.create(
            test=self.test,
            question_text='¿Cuál es la capital de Francia?'
        )
        # crear un estudiante de prueba
        self.student = Student.objects.create(
            user=self.user,
            address='123 Main St',
            whatsapp='555-5555'
        )

        # crear una respuesta de estudiante de prueba para la pregunta
        self.student_answer = StudentAnswer.objects.create(
            question=self.question,
            student=Student.objects.get(user=self.user),
            answer_text='Paris'
        )

    def test_post_student_answer(self):
        # autenticar el cliente con el usuario de prueba
        #self.client.force_authenticate(user=self.user)

        # datos de la respuesta de estudiante
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

        # comprobar que se recibe una respuesta 201 CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # comprobar que la respuesta devuelta coincide con la respuesta de estudiante creada anteriormente
        self.assertNotEqual(response.data, StudentAnswerSerializer(
            self.student_answer).data)
        self.assertEqual(response.data['answer_text'],'Londres')
