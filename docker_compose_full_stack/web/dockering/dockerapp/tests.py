from django.test import TestCase


class TestDockerApp(TestCase):

    def test_dockerapp(self):
        response = self.client.get("/dockerapp/")
        self.assertEqual(200, response.status_code)

    def test_foos(self):
        # test POST
        payload = {"title": "myfoo"}
        response = self.client.post("/dockerapp/foos/", data=payload)
        self.assertEqual(201, response.status_code)
        new_foo = response.json()
        self.assertEqual("myfoo", new_foo["title"])
        import ipdb; ipdb.set_trace();  # XXX Breakpoint

        # test GET
        response = self.client.get("/dockerapp/foos/")
        foos = response.json()
        self.assertIn(new_foo, foos)
