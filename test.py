import json
for i in range(100):
    with open('Indian_Number_plates.json') as json_data:
        data_dict = json.load(json_data)

    data_str = json.dumps(data_dict)

    data_dict_02 = json.loads(data_str)
    print(data_dict_02)