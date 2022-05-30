import unittest
import requests


TARGET_URL = 'https://playground.learnqa.ru/api/'
HTTP_OK = 200

class TestMyLoginUrl(unittest.TestCase):

    def setUp(self) -> None:
        print(f'Start test--------------------------------')

    def test_login_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234',
        }
        response = requests.post(f'{TARGET_URL}user/login', data=data)
        self.assertEqual(response.status_code, HTTP_OK)
        print(response.headers)

        auth_sid = response.cookies["auth_sid"]
        token = response.headers["x-csrf-token"]

    def test_creat_user(self):
        reg_data = {
            'username': 'Vasia',
            'firstName': 'Pupkin',
            'lastName': 'Po',
            'email': 'test_user30.05.2022@example.com',
            'password': '1234',
        }
        response = requests.post(f'{TARGET_URL}user/login', data=reg_data)
        self.assertEqual(response.status_code, HTTP_OK)
        data = response.json()
        user_id = data['id']
        self.assertTrue('id' in list(data.keys()))

        #Дальше снова можно логиниться
        log_data = {
            'email': 'test_user30.05.2022@example.com',
            'password': '1234',
        }
        response = requests.post(f'{TARGET_URL}user/login', data=log_data)
        self.assertEqual(response.status_code, HTTP_OK)
        print(response.headers)

        auth_sid = response.cookies["auth_sid"]
        token = response.headers["x-csrf-token"]

        #Удаление
        response = requests.delete(
            f'{TARGET_URL}user/{user_id}',
            headers={'x-csrf-token':token},
            cookies={'auth_sid':auth_sid},
        )


    def tearDown(self) -> None:
        print(f'Stop test --------------------------------')


if __name__ == '__main__':
    unittest.main()
