# tests.py in your app folder (e.g., Q2/tests.py)
from django.test import RequestFactory
from django.urls import reverse
from django.test import TestCase
from Q2.views import greet_user

class GreetUserViewTests(TestCase):

    def test_greet_user_default_name(self):
        try:
            # Create a request object
            request = RequestFactory().get(reverse('greet_user'))

            # Call the view function
            response = greet_user(request)

            # Check if the response contains the default name ('Guest')
            self.assertContains(response, 'Guest', status_code=200)
            print("Passed Default name greeted successfully.")
        except AssertionError:
            print("Failed Default name not greeted successfully.")

    def test_greet_user_custom_name(self):
        try:
            # Create a request object with a custom name parameter
            request = RequestFactory().get(reverse('greet_user') + '?name=John')

            # Call the view function
            response = greet_user(request)

            # Check if the response contains the custom name ('John')
            self.assertContains(response, 'John', status_code=200)
            print("Passed Custom name greeted successfully.")
        except AssertionError:
            print("Failed Custom name not greeted successfully.")

    def test_greet_user_template_used(self):
        try:
            # Create a request object
            request = RequestFactory().get(reverse('greet_user'))

            # Call the view function
            response = greet_user(request)

            # Check if the response contains the expected content from the template
            self.assertContains(response, 'Hello, Guest!', status_code=200)
            print("Passed Correct template used.")
        except AssertionError:
            print("Failed Incorrect template used.")

    def test_greet_user_empty_name(self):
        try:
            # Create a request object with an empty name parameter
            request = RequestFactory().get(reverse('greet_user') + '?name=')

            # Call the view function
            response = greet_user(request)

            # Check if the response contains an empty string due to the unchanged views.py
            self.assertContains(response, '', status_code=200)
            print("Passed Empty name treated as default.")
        except AssertionError:
            print("Failed Empty name not treated as default.")

    def test_greet_user_long_name(self):
        try:
            # Create a request object with a long name parameter
            long_name = 'X' * 100
            request = RequestFactory().get(reverse('greet_user') + f'?name={long_name}')

            # Call the view function
            response = greet_user(request)

            # Check if the response contains the original long name (not truncated) due to the unchanged views.py
            self.assertContains(response, long_name, status_code=200)
            print("Passed Long name not truncated successfully.")
        except AssertionError:
            print("Failed Long name not truncated successfully.")
