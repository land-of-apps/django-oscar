from django.test import TestCase, Client
from django.urls import reverse
from time import sleep

class RateLimitTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('captcha_view')  # Replace with the actual view name

    def test_rate_limit_exceeded(self):
        # Simulate requests to exceed the rate limit
        for _ in range(6):  # Assuming the limit is 5 requests per minute
            response = self.client.get(self.url)
            if _ < 5:
                self.assertEqual(response.status_code, 200)
            else:
                self.assertEqual(response.status_code, 429)  # HTTP 429 Too Many Requests

    def test_rate_limit_edge_case(self):
        # Test exactly at the limit
        for _ in range(5):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, 200)

        # Wait for the rate limit to reset (assuming 1 minute)
        sleep(60)

        # Test again after reset
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
