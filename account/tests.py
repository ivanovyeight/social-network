from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from account.models import Profile
from account.forms import UserRegistrationForm, ProfileEditForm


class AccountTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='whoami', password='pass')
        Profile.objects.create(user=self.user)
        self.client.login(username='whoami', password='pass')

    # FORMS
    def test_user_registration_form_is_valid(self):
        data = {'username': 'testuser', 'password': 'q', 'password2': 'qw'}
        form = UserRegistrationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_profile_edit_form_is_valid(self):
        data = {'date_of_birth': 'qqq'}
        self.client.post("edit", data)
        profile_form = ProfileEditForm(data=data)
        self.assertFalse(profile_form.is_valid())

    # URLS
    def test_users_list_url_is_resolved(self):
        response = self.client.get(reverse("user_list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.user, response.context['users'])

    def test_user_detail_url_is_resolved(self):
        response = self.client.get(reverse("user_detail", args=[self.user]))
        self.assertEqual(response.status_code, 200)

    def test_user_edit_url_is_resolved(self):
        response = self.client.get(reverse("edit"))
        self.assertEqual(response.status_code, 200)

    def test_user_dashboard_url_is_resolved(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_register_url_is_resolved(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_login_url_is_resolved(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_logout_url_is_resolved(self):
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)

    def test_password_change_url_is_resolved(self):
        response = self.client.get(reverse("password_change"))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_url_is_resolved(self):
        response = self.client.get(reverse("password_reset"))
        self.assertEqual(response.status_code, 200)
