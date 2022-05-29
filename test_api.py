import unittest
import requests

Target_api = 'https://www.breakingbadapi.com/api/'
HTTP_OK = 200
Total_characters = 62

class TestMyApi(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_fetch_all_characters(self):
        response = requests.get(f'{Target_api}characters')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(len(response.json()), Total_characters, f'expecting fetch data about {Total_characters}')

    def test_fetch_1_characters(self):
        response = requests.get(f'{Target_api}characters/1')
        self.assertEqual(response.status_code, HTTP_OK)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['char_id'], 1)
        self.assertEqual(data[0]['name'], 'Walter White')

    def test_fetch_all_quotes_from_a_series(self):
        response = requests.get(f'{Target_api}quotes?series=Better+Call+Saul')
        self.assertEqual(response.status_code, HTTP_OK)
        self.assertEqual(len(response.json()), 18)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()
