import requests
import json


def getData_source_1():
    print("Getting data from API................")
    data=requests.get("https://randomuser.me/api/?results=5000").json()
    # print(json.dumps(data,indent=4))
    return data

def filterData():
    filtered_data=[]
    data=getData_source_1()

    print("Writing Data to JSON file.......")
    for person in data['results']:
        person_dict={}
        person_dict['name']=person['name']['title']+'. '+person['name']['first']+person['name']['last']
        person_dict['email']=person['email']
        person_dict['username']=person['login']['username']
        person_dict['phone']=person['cell']
        person_dict['profile']=person['picture']['large']
        person_dict['age']=person['dob']['age']

        filtered_data.append((person_dict))


    with open("filtered_data.json","w") as f:
        json_string=json.dumps(filtered_data,indent=4)
        f.write(json_string)

    print("Sucessfully wrote data to JSON file...........")

filterData()

# getData_source_1()