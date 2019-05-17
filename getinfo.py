import requests

header = {'Authorization': 'Bearer '+'pNVmeIrIh2DyXJLTe7NLlnWgDWQ7qSoM'}
#get_response = requests.get('https://api.box.com/2.0/search?query=testone&type=folder&fields=name', headers=header)
#print(get_response.json())

folder_id_array = ['76631879425','76629705275']
put_url = 'https://api.box.com/2.0/folders/'
folder_id = '76629705275'
put_data = '{"name": "test_python123"}'
for id in folder_id_array:
    put_response = requests.put(put_url+id, data=put_data, headers=header)
    print(put_response.status_code)