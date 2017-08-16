from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.test import force_authenticate

from show.factories import create_data
from . import views

User = get_user_model()


class MyTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super(MyTestCase, cls).setUpClass()
        cls.request_factory = APIRequestFactory()
        cls.client = APIClient()
        create_data()
        # We told factory the first username would be user0
        cls.mentor = User.objects.get(username='user0')
        cls.candidate = User.objects.get(name='candidate0')

    def test_login_with_valid_credentials_succeed(self):
        create_data()
        response = self.client.post('/api/v1/login/', {
            'username': 'user0',
            'password': 'valid'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('key', response.data)

    def test_login_with_invalid_credentials_failed(self):
        response = self.client.post('/api/v1/login/', {
            'username': 'user0',
            'password': 'invalid'})
        self.assertEqual(response.status_code, 400)

    def test_listing_teams(self):
        request = self.request_factory.get('')
        team_lists = views.MentorTeamViewSet.as_view({'get': 'list'})
        force_authenticate(request, user=self.mentor)
        response = team_lists(request)
        self.assertEqual(response.status_code, 200)
        # Check if if has got his team average score or not
        self.assertIn('team_average_score', response.data[0])
        # Check if there are candidates or not
        self.assertIn('candidates', response.data[0])

    def test_candidate_detail(self):
        request = self.request_factory.get('')
        candidate_detail = views.CandidateDetailView.as_view()
        force_authenticate(request, user=self.mentor)
        response = candidate_detail(request, pk=self.candidate.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIn('activities', response.data)