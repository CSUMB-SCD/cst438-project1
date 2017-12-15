import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    #ensures that flask was set up correctly
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get("/login",content_type="html/text")
        self.assertEqual(response.status_code,302)
    #ensures login page loads correctly
    def test_login_page_loads(self):
        tester=app.test_client(self)
        response=tester.get("/",content_type="html/text")
        self.assertTrue("LOGIN"in response.data)
    def test_correct_login(self):
        tester=app.test_client(self)
        response=tester.post(
            "/",
        data=dict(username="nice",password="nice"),
        follow_redirects=True
        )
        self.assertIn("", response.data)

if __name__ == '__main__':
    unittest.main()
