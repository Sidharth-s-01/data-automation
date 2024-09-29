

import json

with open("filtered_data.json","r") as f:
    print("Transforming data based on certain conditions....")
    data=json.load(f)
    for person in data:
        if person['age']>50:
            person["Above_Age"]=True
        else:
            person["Above_Age"]=False

    with open("Transformed.json","w") as f:
        json_string=json.dumps(data,indent=4)
        f.write(json_string)

    print("Data has been Transformed and copied to Transform.json......")
    # print(data)