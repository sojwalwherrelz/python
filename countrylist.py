import requests
import json

apikey = "%APIKEY%"
response = requests.get("https://api.cricapi.com/v1/countries?apikey="+apikey+"&offset=0")
def myobj(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    data = json.loads(text)['data']
    # print(data)
    print("----------------------------Country List -----------------")
    for value in data:
        print(value['name']+"  - "+value['genericFlag'])    

myobj(response.json())
