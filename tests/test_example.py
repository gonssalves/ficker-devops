import unittest
import requests

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://localhost:5000'

    def test_index_route(self):
        response = requests.get(self.base_url + '/test', timeout=10)  # Tempo de espera de 10 segundos
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Hell, world!')

if __name__ == '__main__':
    unittest.main()
