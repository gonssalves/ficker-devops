import unittest
import requests

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://127.0.0.1:5000'

    def test_index_route(self):
        response = requests.get(self.base_url + '/test')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
