import unittest
import requests

Target_api_les1 = 'https://www.breakingbadapi.com/api/'
Target_api_les2 = 'https://jsonplaceholder.typicode.com/'
HTTP_OK = 200
Total_characters = 62
payload = {
    'userId': 1,
    'title': 'foo_my',
    'body': 'bar_my',
}
payload_put = {
    'userId': 1,
    'id': 1,
    'title': 'foo_my',
    'body': 'bar_my',
}
payload_patch = {
    'title': 'foo_my',
}

# class TestMyApi(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print('Test Lesson_1, ----------------')
#
#     def test_fetch_all_characters(self):
#         response = requests.get(f'{Target_api_les1}characters')
#         self.assertEqual(response.status_code, HTTP_OK)
#         self.assertEqual(len(response.json()), Total_characters, f'expecting fetch data about {Total_characters}')
#
#     def test_fetch_1_characters(self):
#         response = requests.get(f'{Target_api_les1}characters/1')
#         self.assertEqual(response.status_code, HTTP_OK)
#         data = response.json()
#         self.assertEqual(len(data), 1)
#         self.assertEqual(data[0]['char_id'], 1)
#         self.assertEqual(data[0]['name'], 'Walter White')
#
#     def test_fetch_all_quotes_from_a_series(self):
#         response = requests.get(f'{Target_api_les1}quotes?series=Better+Call+Saul')
#         self.assertEqual(response.status_code, HTTP_OK)
#         self.assertEqual(len(response.json()), 18)
#
#     def tearDown(self) -> None:
#         print('End test_lesson_1-----------------')
#
#
# class TestMyLesoon2(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print('Test Lesson_2, -------------------------------------')
#
#     def test_fetch_all_post(self):
#         response = requests.get(f'{Target_api_les2}posts/')
#         self.assertEqual(response.status_code, HTTP_OK)
#         self.assertEqual(len(response.json()), 100)
#
#     def test_fetch_one_post(self):
#         response = requests.get(f'{Target_api_les2}posts/1/')
#         # проверка на статус сервера 200
#         self.assertEqual(response.status_code, HTTP_OK)
#         # проверка ключей словаря
#         data = response.json()
#         actual_keys = list(data.keys())
#         expected_keys = ['userId', 'id', 'title', 'body']
#         for i in range(len(actual_keys)):
#             self.assertEqual(actual_keys[i], expected_keys[i])
#         # self.assertEqual(actual_keys, expected_keys)
#         # проверка длинны
#         self.assertEqual(len(data), 4)
#         # проверка совпадения ключа и значения
#         self.assertEqual(data['id'], 1)
#
#     def test_1_post_post(self):
#         response = requests.post(f'{Target_api_les2}posts', data=payload)
#         data = response.json()
#         actual_values = list(data.values())
#         expected_values = ['1', 'foo_my', 'bar_my', 101]
#         for i in range(len(actual_values)):
#             self.assertEqual(actual_values[i], expected_values[i])
#
#     def test_2_put_post(self):
#         response = requests.put(f'{Target_api_les2}posts/1', data=payload_put)
#         data = response.json()
#         actual_values = list(data.values())
#         expected_values = ['1', 1, 'foo_my', 'bar_my']
#         for i in range(len(actual_values)):
#             self.assertEqual(actual_values[i], expected_values[i])
#
#     def test_3_patch_post(self):
#         response = requests.patch(f'{Target_api_les2}posts/1', data=payload_patch)
#         data = response.json()
#         actual_keys = data['title']
#         expected_keys = 'foo_my'
#         self.assertEqual(actual_keys, expected_keys)
#
#     def test_4_delete_post(self):
#         response = requests.delete(f'{Target_api_les2}posts/1')
#         self.assertEqual(response.status_code, HTTP_OK)
#
#     def tearDown(self) -> None:
#         print('End test_lesson_2 --------------------------------------')


if __name__ == '__main__':
    unittest.main()
