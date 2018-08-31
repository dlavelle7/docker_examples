from django.test import TestCase


class TestDockerApp(TestCase):

    def test_dockerapp(self):
        response = self.client.get("/dockerapp/")
        self.assertEqual(200, response.status_code)
