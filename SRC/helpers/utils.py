# helps you to read the json file and provide the data

import json

def get_payload_auth():
    # read from the auth.json and return json
    f=open("SRC/resourses/auth.json", "r")
    data=f.read()
    #data= json.loads(f.read())
    file_data=json.loads(data)
    print(file_data)
    f.close()

get_payload_auth()



