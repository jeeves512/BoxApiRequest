import requests

header = {'Authorization': 'Bearer '+'pVnqHSYrzp03RAlSQ9ZkxrwOhL6H4Xzf'}
query = 'Partner Safeguarding Policies and Procedures Test Prime'
endpoint = 'https://api.box.com/2.0/search?query='+query+'&type=folder&fields=name'
get_response = requests.get(endpoint, headers=header)
output = get_response.json()
folder_id_array = []
name_check = False
print(output)
for x in output:
    if x == 'entries':
        for entries in output[x]:
            for entries_info in entries:
                if entries_info == 'id' and entries['name'] == query:
                    folder_id_array.append(entries[entries_info])
                    name_check = False

put_url = 'https://api.box.com/2.0/folders/'
put_data = '{"name": "Partner Safeguarding Policies and Procedures Test 123"}'
for x in folder_id_array:
    print(x)
for id in folder_id_array:
    put_response = requests.put(put_url+id, data=put_data, headers=header)
    print(put_response.status_code)