"""
Lesson2
"""
import requests

Target_api_les2 = 'https://jsonplaceholder.typicode.com/'
# response = requests.get(f'{Target_api_les2}posts/')
# data = response.json()
# print(data)
# print(data[0]['userId'])
# print(data[0]['id'])
# print(data[0]['title'])
# print('-----------')
# response2 = requests.get(f'{Target_api_les2}posts/1/')
# data2 = response2.json()
# print(data2)
# print('-----------')
# expected_keys = ['userId', 'id', 'title', 'body']
# actual_keys = list(data2.keys())
# for i in range(len(actual_keys)):
#    print(actual_keys[i])
#    print(expected_keys[i])



# print('-----------')
# payload = {
#     'title': 'foo_my',
#     'body': 'bar_my',
#     'userId': 1,
# }
# payload_new = {
#     'id': 1,
#     'title': 'foo_my',
#     'body': 'bar_my',
#     'userId': 1,
# }
# response3 = requests.post(f'{Target_api_les2}posts', data=payload)
# data3 = response3.json()
# print(data3)
#
# response4 = requests.put(f'{Target_api_les2}posts/1', data=payload_new)
# data4 = response4.json()
# print(data4)


di = {'userId': '1', 'title': 'foo_my', 'body': 'bar_my', 'id': 101}
lst = ['1', 'foo_my', 'bar_my', 101]

act = di.values()
print(act)