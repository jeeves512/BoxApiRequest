import requests

# get request is used to get the folder ids of all the files that needs to be renamed
header = {'Authorization': 'Bearer '+'pVnqHSYrzp03RAlSQ9ZkxrwOhL6H4Xzf'}
# name of file that needs to be renamed
query = 'Test Prime'     
endpoint = 'https://api.box.com/2.0/search?query='+query+'&type=folder&fields=name'
get_response = requests.get(endpoint, headers=header)
# gets the output in json
output = get_response.json()
# array to store folder ids
folder_id_array = []  

# output from the get request contains a lot of data.
# The output is filtered to find the folder ids of folders matching the query name.
for x in output:  
    if x == 'entries':
        for entries in output[x]:
            for entries_info in entries:
                if entries_info == 'id' and entries['name'] == query:
                    folder_id_array.append(entries[entries_info])
                    
                    
# put request to rename the folders
put_url = 'https://api.box.com/2.0/folders/'
put_data = '{"name": "New Name"}'
# iterates through folder ids to change endpoint of the put request
for id in folder_id_array:  
    put_response = requests.put(put_url+id, data=put_data, headers=header)
    # print status code to make sure request was successfull
    print(put_response.status_code)  
