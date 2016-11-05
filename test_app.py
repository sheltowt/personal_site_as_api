import unittest
import app
from app import resume
import json

class AppTestCases(unittest.TestCase):

    def setUp(self):
        self.app = app.basic_api.test_client()

    def test_get_tasks(self):
        response = self.app.get('/')
        data = json.loads(response.data)
        self.assertEqual(data, resume)

if __name__ == '__main__':
    unittest.main()