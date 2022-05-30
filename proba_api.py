import requests

Target_api_les1 = 'https://www.breakingbadapi.com/api/'

# response = requests.get(f'{Target_api}characters')
# response_1 = requests.get(f'{Target_api}characters/1')
response_2 = requests.get(f'{Target_api_les1}quotes?series=Better+Call+Saul')

# print(response)
# print(len(response.json()))
# data = response_1.json()
# print(data[0].name)
#
# for i in data:
#     data_dict = dict(i)

# print(data_dict['char_id'])
# print(data_dict['name'])
data_1 = response_2.json()
print(len(data_1))
# print(data_1)
print(data_1[1]['quote'])
