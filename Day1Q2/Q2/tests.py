# tests.py in your app folder (e.g., Q2/tests.py)
from django.test import RequestFactory
from django.urls import reverse
from Q2.views import greet_user

def test_greet_user_default_name():
    try:
        # Create a request object
        request = RequestFactory().get(reverse('greet_user'))

        # Call the view function
        response = greet_user(request)

        # Check if the response contains the default name ('Guest')
        assert 'Guest' in str(response.content)
        print("Passed Default name greeted successfully.")
    except AssertionError:
        print("Failed Default name not greeted successfully.")

def test_greet_user_custom_name():
    try:
        # Create a request object with a custom name parameter
        request = RequestFactory().get(reverse('greet_user') + '?name=John')

        # Call the view function
        response = greet_user(request)

        # Check if the response contains the custom name ('John')
        assert 'John' in str(response.content)
        print("Passed Custom name greeted successfully.")
    except AssertionError:
        print("Failed Custom name not greeted successfully.")

def test_greet_user_template_used():
    try:
        # Create a request object
        request = RequestFactory().get(reverse('greet_user'))

        # Call the view function
        response = greet_user(request)

        # Check if the response contains the expected content from the template
        assert 'Hello, Guest!' in str(response.content)
        print("Passed Correct template used.")
    except AssertionError:
        print("Failed Incorrect template used.")

def test_greet_user_empty_name():
    try:
        # Create a request object with an empty name parameter
        request = RequestFactory().get(reverse('greet_user') + '?name=')

        # Call the view function
        response = greet_user(request)

        # Check if the response contains the default name ('Guest')
        assert 'Guest' in str(response.content)
        print("Passed Empty name treated as default.")
    except AssertionError:
        print("Failed Empty name not treated as default.")

def test_greet_user_long_name():
    try:
        # Create a request object with a long name parameter
        long_name = 'X' * 100
        request = RequestFactory().get(reverse('greet_user') + f'?name={long_name}')

        # Call the view function
        response = greet_user(request)

        # Check if the response contains the truncated name
        assert '...' in str(response.content)
        print("Passed Long name truncated successfully.")
    except AssertionError:
        print("Failed Long name not truncated successfully.")