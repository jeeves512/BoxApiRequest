import requests

# get request is used to get the folder ids of all the files that needs to be renamed
header = {'Authorization': 'Bearer '+'pVnqHSYrzp03RAlSQ9ZkxrwOhL6H4Xzf'}
query = 'Test Prime'     # name of file that needs to be renamed
endpoint = 'https://api.box.com/2.0/search?query='+query+'&type=folder&fields=name'
get_response = requests.get(endpoint, headers=header)
output = get_response.json() # gets the output in json
folder_id_array = []  #array to store folder ids

# output from the get request contains a lot of data.
# The output is filtered to find the folder ids of folders matching the query name.
for x in output:  # traverses the output from get request to store folder id
    if x == 'entries':
        for entries in output[x]:
            for entries_info in entries:
                if entries_info == 'id' and entries['name'] == query:
                    folder_id_array.append(entries[entries_info])
                    
                    
# put request to rename the folders
put_url = 'https://api.box.com/2.0/folders/'
put_data = '{"name": "New Name"}'
for id in folder_id_array:  # iterates through folder ids to change endpoint of the put request
    put_response = requests.put(put_url+id, data=put_data, headers=header)
    print(put_response.status_code)  # print status code to make sure request was successfull
